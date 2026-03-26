from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from reports.models import Issue, Notification
from reports.utils import auto_escalate_issues, create_notification


# =========================
# PUBLIC PAGES
# =========================


def index(request):

    unread_count = 0  # default

    if request.user.is_authenticated:

        role = request.user.userprofile.user_type

        # 🔁 Redirect other roles
        if role == 'department':
            return redirect('department')

        elif role == 'worker':
            return redirect('worker_portal')

        elif role == 'head':
            return redirect('headAuthority')

        # 👤 Citizen stays here
        elif role == 'citizen':

            unread_count = Notification.objects.filter(
                user=request.user,
                is_read=False
            ).count()

            return render(request, 'frontend/index.html', {
                'unread_count': unread_count
            })

    # 👤 Not logged in
    return render(request, 'frontend/index.html', {
        'unread_count': unread_count
    })


@login_required(login_url='login')
def department(request):

    # 🔥 Auto escalation check
    auto_escalate_issues()

    # 🔥 Get department
    dept = request.user.userprofile.department

    # 🔥 Filter issues
    pending_issues = Issue.objects.filter(
        issue_type=dept,
        status='pending',
        is_escalated=False
    )

    active_issues = Issue.objects.filter(
        issue_type=dept,
        status='in_progress',
        is_escalated=False
    )

    escalated_issues = Issue.objects.filter(
        issue_type=dept,
        is_escalated=True
    )

    # 🔥 Get workers of same department
    workers = User.objects.filter(
        userprofile__user_type='worker',
        userprofile__department=dept
    )

    # ================= ASSIGN WORK =================
    if request.method == 'POST':

        issue_id = request.POST.get('issue_id')
        worker_id = request.POST.get('worker')

        issue = get_object_or_404(Issue, id=issue_id)
        worker = get_object_or_404(User, id=worker_id)

        # Assign worker
        issue.worker = worker
        issue.status = 'in_progress'
        issue.save()

        # 🔔 NOTIFICATION TO WORKER
        create_notification(
            worker,
            f"You have been assigned a {issue.issue_type} issue at {issue.location}"
        )

        return redirect('department')

    # ================= RESPONSE =================
    return render(request, 'frontend/department.html', {
        'pending_issues': pending_issues,
        'active_issues': active_issues,
        'escalated_issues': escalated_issues,
        'workers': workers
    })


@login_required(login_url='login')
def reports(request):
    return render(request, 'frontend/reports.html')


@login_required(login_url='login')
def headAuthority(request):

    issues = Issue.objects.all().order_by('-created_at')

    # 🔔 Notifications for this user
    notification_list = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    unread_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    context = {
        "issues": issues,
        "total_count": issues.count(),
        "escalated_count": issues.filter(is_escalated=True).count(),
        "inprogress_count": issues.filter(status="in_progress").count(),
        "resolved_count": issues.filter(status="resolved").count(),

        # 🔔 add this
        "notification_list": notification_list,
        "unread_count": unread_count,
    }

    return render(request, "frontend/headAuthority.html", context)

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

    # 🔥 Issues assigned to worker
    issues = Issue.objects.filter(worker=request.user)

    # 🔔 Notifications for worker
    notification_list = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    unread_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    # ================= UPDATE STATUS =================
    if request.method == "POST":
        issue_id = request.POST.get("issue_id")
        status = request.POST.get("status")

        issue = get_object_or_404(Issue, id=issue_id)

        issue.status = status
        issue.save()

        return redirect('worker_portal')

    # ================= RESPONSE =================
    return render(request, 'frontend/worker_portal.html', {
        "issues": issues,

        # 🔔 notification data
        "notification_list": notification_list,
        "unread_count": unread_count
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

            # admin
            if profile.user_type == 'admin':
                return redirect('admin_dashboard')
            
            # Department
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

@login_required
def admin_dashboard(request):

    total_users = User.objects.count()
    total_issues = Issue.objects.count()

    pending = Issue.objects.filter(status='pending').count()
    resolved = Issue.objects.filter(status='resolved').count()

    recent_issues = Issue.objects.order_by('-created_at')[:5]

    context = {
        "total_users": total_users,
        "total_issues": total_issues,
        "pending": pending,
        "resolved": resolved,
        "recent_issues": recent_issues
    }

    return render(request, "frontend/admin_dashboard.html", context)


@login_required(login_url='login')
def citizen_list(request):

    if request.user.userprofile.user_type != 'admin':
        return HttpResponseForbidden("Access denied")

    citizens = User.objects.filter(
        userprofile__user_type='citizen'
    )

    return render(request, 'frontend/citizen_list.html', {
        'citizens': citizens
    })


@login_required(login_url='login')
def department_list(request):

    if request.user.userprofile.user_type != 'admin':
        return HttpResponseForbidden("Access denied")

    departments = User.objects.filter(
        userprofile__user_type='department'
    )

    return render(request, 'frontend/department_list.html', {
        'departments': departments
    })


@login_required(login_url='login')
def worker_list(request):

    if request.user.userprofile.user_type != 'admin':
        return HttpResponseForbidden("Access denied")

    workers = User.objects.filter(
        userprofile__user_type='worker'
    )

    return render(request, 'frontend/worker_list.html', {
        'workers': workers
    })