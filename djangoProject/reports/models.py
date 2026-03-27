from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


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

    # deadline
    deadline = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # ================= DEADLINE =================
    def set_deadline(self):

        BASE_TIME = {
            'water': 1,
            'electricity': 1,
            'garbage': 2,
            'road': 3,
        }

        base_days = BASE_TIME.get(self.issue_type, 2)

        # 🔥 check if authority rule exists
        rule = DepartmentRule.objects.filter(
            department=self.issue_type
        ).first()

        if rule:
            base_days = rule.get_effective_time()  # ✅ 24h logic handled here

        self.deadline = timezone.now() + timedelta(days=base_days)

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
    

class DepartmentRule(models.Model):

    DEPARTMENTS = [
        ('road', 'Road'),
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('garbage', 'Garbage'),
    ]

    department = models.CharField(max_length=50, choices=DEPARTMENTS)

    # penalty time (e.g. 0.5 day)
    time_limit = models.FloatField(default=1)

    # 🔥 when penalty was applied
    penalty_applied_at = models.DateTimeField(null=True, blank=True)

    def is_penalty_active(self):
        if self.penalty_applied_at:
            return timezone.now() < self.penalty_applied_at + timedelta(hours=24)
        return False

    def get_effective_time(self):
        BASE_TIME = {
            'water': 1,
            'electricity': 1,
            'garbage': 2,
            'road': 3,
        }

        base = BASE_TIME.get(self.department, 1)

        if self.is_penalty_active():
            return self.time_limit  # apply penalty
        return base  # reset after 24h

    def __str__(self):
        return f"{self.department} - {self.time_limit} day(s)"