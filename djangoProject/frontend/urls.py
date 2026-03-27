from django.urls import include, path

from reports import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('worker_portal/', views.worker_portal, name='worker_portal'),
    path('department/', views.department, name='department'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('citizen_list/', views.citizen_list, name='citizen_list'),
    path('department_list/', views.department_list, name='department_list'),
    path('department_performance/', views.department_performance, name='department_performance'),
    path('action/<str:issue_type>/', views.action, name='action'),
    path('workers_list/', views.worker_list, name='worker_list'),
    path('reports/', include('reports.urls')),
    path('headAuthority/', views.headAuthority, name='headAuthority'),
    path('manage_workers/', views.manage_workers, name='manage_workers'),
    path('view_reports/', views.view_reports, name='view_reports'),
]
