from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from reports.models import Issue


# =========================
# PUBLIC PAGES
# =========================

def index(request):
    return render(request, 'frontend/index.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from reports.models import Issue


@login_required(login_url='login')
def department(request):

    # Get department of logged-in user
    dept = request.user.userprofile.department

    # Filter issues based on department
    pending_issues = Issue.objects.filter(
        issue_type=dept,
        status='pending'
    )

    active_issues = Issue.objects.filter(
        issue_type=dept,
        status='in_progress'
    )

    # Get workers belonging to the same department
    workers = User.objects.filter(
        userprofile__user_type='worker',
        userprofile__department=dept
    )

    # Assign worker to issue
    if request.method == 'POST':
        issue_id = request.POST.get('issue_id')
        worker_id = request.POST.get('worker')

        issue = get_object_or_404(Issue, id=issue_id)
        worker = get_object_or_404(User, id=worker_id)

        issue.worker = worker
        issue.status = 'in_progress'
        issue.save()

        return redirect('department')

    return render(request, 'frontend/department.html', {
        'pending_issues': pending_issues,
        'active_issues': active_issues,
        'workers': workers
    })

@login_required(login_url='login')
def reports(request):
    return render(request, 'frontend/reports.html')

@login_required(login_url='login')
def headAuthority(request):
    return render(request, 'frontend/headAuthority.html')

@login_required(login_url='login')
def manage_workers(request):

    department = request.user.userprofile.department

    workers = User.objects.filter(
        userprofile__user_type='worker',
        userprofile__department=department
    )

    return render(request, 'frontend/manage_workers.html', {
        'workers': workers
    })

@login_required(login_url='login')
def worker_portal(request):

    issues = Issue.objects.filter(worker=request.user)

    if request.method == "POST":
        issue_id = request.POST.get("issue_id")
        status = request.POST.get("status")

        issue = get_object_or_404(Issue, id=issue_id)

        issue.status = status
        issue.save()

        return redirect('worker_portal')

    return render(request, 'frontend/worker_portal.html', {
        "issues": issues
    })

def view_reports(request):

    issues = Issue.objects.all().order_by('-created_at')

    return render(request, 'frontend/my_reports.html', {
        'issues': issues
    })

def logout_view(request):
    logout(request)
    return render(request, 'frontend/logout.html')

# =========================
# LOGIN
# =========================

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.models import UserProfile


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ensure profile exists
            profile, created = UserProfile.objects.get_or_create(user=user)

            # Department users
            if profile.user_type == 'department':
                return redirect('department')

            # Worker
            elif profile.user_type == 'worker':
                return redirect('worker_portal')

            # Head authority
            elif profile.user_type == 'head':
                return redirect('headAuthority')

            # Citizen
            elif profile.user_type == 'citizen':
                return redirect('index')

            # fallback
            else:
                return redirect('index')

        else:
            return render(request, 'frontend/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'frontend/login.html')
# =========================
# REGISTER
# =========================

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'frontend/register.html')
