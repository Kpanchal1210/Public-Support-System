from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('worker_portal/', views.worker_portal, name='worker_portal'),
    path('department/', views.department, name='department'),
    path('reports/', views.reports, name='reports'),
    path('headAuthority/', views.headAuthority, name='headAuthority'),
]
