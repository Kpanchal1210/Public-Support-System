from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('worker_portal/', views.worker_portal, name='worker_portal'),
    path('department/', views.department, name='department'),
    path('reports/', include('reports.urls')),
    path('headAuthority/', views.headAuthority, name='headAuthority'),
]
