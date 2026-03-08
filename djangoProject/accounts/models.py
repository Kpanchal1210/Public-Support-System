from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    USER_TYPES = (
        ('citizen', 'Citizen'),
        ('garbage', 'Garbage Department'),
        ('water', 'Water Department'),
        ('electricity', 'Electricity Department'),
        ('road', 'Road Department'),
        ('worker', 'Worker'),
        ('head', 'Head Authority'),
    )

    DEPARTMENTS = ( 
        ('garbage', 'Garbage'), 
        ('water', 'Water'), 
        ('electricity', 'Electricity'), 
        ('road', 'Road'), 
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    department = models.CharField(max_length=20, choices=DEPARTMENTS, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
