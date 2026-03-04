from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_type', 'citizen', 'status', 'created_at')
    list_filter = ('issue_type', 'status')
    search_fields = ('location', 'description')