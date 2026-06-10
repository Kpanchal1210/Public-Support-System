from celery import shared_task
from django.utils import timezone

from .models import Issue


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