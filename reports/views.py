from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import IssueForm

@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)

        if form.is_valid():
            issue = form.save(commit=False)
            issue.citizen = request.user
            issue.save()

            messages.success(request, "Your issue has been submitted successfully!")

            return redirect('report_issue')

    else:
        form = IssueForm()

    return render(request, 'frontend/reports.html', {'form': form})