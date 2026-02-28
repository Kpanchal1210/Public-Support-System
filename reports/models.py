from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):

    ISSUE_TYPES = [
        ('road', 'Road Problem'),
        ('water', 'Water Supply'),
        ('electricity', 'Electricity'),
        ('garbage', 'Garbage'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    citizen = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='issues/', blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status}"