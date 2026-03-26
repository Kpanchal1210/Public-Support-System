from django.utils import timezone
from .models import Issue


def auto_escalate_issues():

    issues = Issue.objects.filter(
        is_escalated=False,
        status__in=['pending', 'in_progress']
    )

    for issue in issues:
        if issue.deadline and timezone.now() > issue.deadline:
            issue.is_escalated = True
            issue.save()


from .models import Notification

def create_notification(user, message):
    Notification.objects.create(
        user=user,
        message=message
    )