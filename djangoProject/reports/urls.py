from django.urls import path
from . import views

urlpatterns = [
    path('report_issue/', views.report_issue, name='report_issue'),
    path('notification/', views.notification, name='notification'),
]