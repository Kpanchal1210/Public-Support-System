from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

from .models import Issue
from .forms import IssueForm


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


@login_required
def department_dashboard(request):

    issues = Issue.objects.all().order_by('-created_at')

    workers = User.objects.filter(groups__name='Worker')

    return render(request, "frontend/department.html", {
        "issues": issues,
        "workers": workers
    })