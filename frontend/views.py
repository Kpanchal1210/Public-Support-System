from django.shortcuts import render

def worker_portal(request):
    return render(request, 'frontend/worker_portal.html')

def department(request):
    return render(request, 'frontend/department.html')

def reports(request):
    return render(request, 'frontend/reports.html')

def headAuthority(request):
    return render(request, 'frontend/headAuthority.html')