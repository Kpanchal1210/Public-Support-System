from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Issue(models.Model):

    ISSUE_TYPES = [
        ('road', 'Road Problem'),
        ('water', 'Water Supply'),
        ('electricity', 'Electricity'),
        ('garbage', 'Garbage'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    citizen = models.ForeignKey(User, on_delete=models.CASCADE)

    worker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_worker'
    )

    description = models.TextField()
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='issues/', blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # 🔥 escalation
    is_escalated = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # ================= PENALTY SYSTEM =================

    @staticmethod
    def get_penalty_factor(issue_type):

        # 🔥 count escalations in last 24 hours ONLY
        recent_escalations = Issue.objects.filter(
            issue_type=issue_type,
            is_escalated=True,
            created_at__gte=timezone.now() - timedelta(days=1)
        ).count()

        if recent_escalations >= 2:
            return 0.5   # heavy penalty
        elif recent_escalations >= 1:
            return 0.75  # medium penalty
        else:
            return 1     # normal

    # ================= DEADLINE =================

    def set_deadline(self):

        BASE_TIME = {
            'water': 1,
            'electricity': 1,
            'garbage': 2,
            'road': 3,
        }

        base_days = BASE_TIME.get(self.issue_type, 2)

        # 🔥 apply penalty
        penalty = Issue.get_penalty_factor(self.issue_type)

        final_days = base_days * penalty

        # 🔥 safety minimum (6 hours)
        final_days = max(final_days, 0.25)

        self.deadline = timezone.now() + timedelta(seconds=30)

    def save(self, *args, **kwargs):
        if not self.deadline:
            self.set_deadline()
        super().save(*args, **kwargs)

    # ================= TIME LEFT =================

    def time_left(self):
        if self.deadline:
            return self.deadline - timezone.now()
        return None

    def formatted_time_left(self):
        if not self.deadline:
            return "No deadline"

        remaining = self.deadline - timezone.now()

        if remaining.total_seconds() <= 0:
            return "Expired"

        days = remaining.days
        hours = remaining.seconds // 3600

        return f"{days}d {hours}h left"

    def __str__(self):
        return f"{self.issue_type} - {self.status}"



class Notification(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message[:20]}"