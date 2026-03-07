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

@login_required(login_url='login')
def worker_portal(request):
    return render(request, 'frontend/worker_portal.html')

@login_required(login_url='login')
def department(request):
    pending_issues = Issue.objects.filter(status='pending')
    active_issues = Issue.objects.filter(status='in_progress')
    workers = User.objects.filter(userprofile__user_type='worker')
    
    if request.method == 'POST':
        issue_id = request.POST.get('issue_id')
        worker_id = request.POST.get('worker')
        
        issue = get_object_or_404(Issue, id=issue_id)
        worker = get_object_or_404(User, id=worker_id)
        issue.worker = worker
        issue.status = 'in_progress'
        issue.save()
        
        messages.success(request, 'Issue allocated successfully!')
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

    workers = User.objects.filter(userprofile__user_type='worker')

    return render(request, 'frontend/manage_workers.html', {
        'workers': workers
    })

def logout_view(request):
    logout(request)
    return render(request, 'frontend/logout.html')

# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # get or create profile safely
            profile, created = UserProfile.objects.get_or_create(user=user)

            if profile.user_type == 'department':
                return redirect('department')

            elif profile.user_type == 'head':
                return redirect('headAuthority')

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
