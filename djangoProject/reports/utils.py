from django.utils import timezone
from .models import Issue
from django.contrib.auth.models import User


from .models import Notification

def create_notification(user, message):
    Notification.objects.create(
        user=user,
        message=message
    )