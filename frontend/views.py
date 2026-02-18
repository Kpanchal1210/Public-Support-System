from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# =========================
# PUBLIC PAGES
# =========================

def index(request):
    return render(request, 'frontend/index.html')


def worker_portal(request):
    return render(request, 'frontend/worker_portal.html')


def department(request):
    return render(request, 'frontend/department.html')


def reports(request):
    return render(request, 'frontend/reports.html')


def headAuthority(request):
    return render(request, 'frontend/headAuthority.html')


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # create session
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
