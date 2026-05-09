from django.utils import timezone
from .models import Issue
from django.contrib.auth.models import User


def auto_escalate_issues():

    issues = Issue.objects.filter(
        is_escalated=False,
        status__in=['pending', 'in_progress']
    )

    for issue in issues:
        if issue.deadline and timezone.now() > issue.deadline:

            # 🔥 mark as escalated
            issue.is_escalated = True
            issue.save()

            # 🔔 notify all authorities
            authorities = User.objects.filter(
                userprofile__user_type='authority'
            )

            for user in authorities:
                create_notification(
                    user,
                    f"🚨 Issue escalated: {issue.issue_type} at {issue.location}"
                )


from .models import Notification

def create_notification(user, message):
    Notification.objects.create(
        user=user,
        message=message
    )