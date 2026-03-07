from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Issue
from .forms import IssueForm
from accounts.models import UserProfile


@login_required
def report_issue(request):

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

