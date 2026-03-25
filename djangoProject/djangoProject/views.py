from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import UserProfile
from reports.models import Issue


@login_required
def admin_dashboard(request):

    # counts
    total_users = UserProfile.objects.count()
    total_issues = Issue.objects.count()
    pending = Issue.objects.filter(status='pending').count()
    resolved = Issue.objects.filter(status='resolved').count()

    context = {
        'total_users': total_users,
        'total_issues': total_issues,
        'pending': pending,
        'resolved': resolved
    }

    return render(request, 'frontend/admin_dashboard.html', context)