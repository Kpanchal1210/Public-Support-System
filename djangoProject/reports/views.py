from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Issue, Notification
from django.http import HttpResponseForbidden
from .forms import IssueForm
from accounts.models import UserProfile


@login_required(login_url='login')
def report_issue(request):

    if request.user.userprofile.user_type != 'citizen':
        return HttpResponseForbidden("Only citizens are allowed to report issues.")
    
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)

        if form.is_valid():
            issue = form.save(commit=False)
            issue.citizen = request.user
            issue.save()

            messages.success(request, "Issue reported successfully!")

            return redirect("report_issue")
    else:
        form = IssueForm()

    return render(request, "frontend/reports.html", {"form": form})


def notification(request):
    notifs = Notification.objects.filter(user=request.user).order_by('-created_at')

    unread_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    # mark as read
    notifs.update(is_read=True)

    return render(request, 'frontend/notification.html', {
        'notifications': notifs,
        'unread_count': unread_count
    })
