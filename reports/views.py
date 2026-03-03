from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IssueForm

@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            return redirect('dashboard')  # change if needed
    else:
        form = IssueForm()

    return render(request, 'frontend/reports.html', {'form': form})