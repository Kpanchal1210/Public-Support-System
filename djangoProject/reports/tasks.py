from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from .models import Issue, Notification


@shared_task
def auto_escalate_issues():

    issues = Issue.objects.filter(
        status__in=['pending', 'in_progress'],
        is_escalated=False,
        deadline__lte=timezone.now()
    )

    count = 0

    for issue in issues:
        issue.is_escalated = True
        issue.save(update_fields=['is_escalated'])
        count += 1

    return f"{count} issues escalated"


@shared_task
def cleanup_notifications():

    cutoff = timezone.now() - timedelta(days=30)

    deleted_count, _ = Notification.objects.filter(
        is_read=True,
        created_at__lt=cutoff
    ).delete()

    return f"Deleted {deleted_count} notifications"