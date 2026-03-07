from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_type', 'citizen', 'status', 'created_at')
    list_filter = ('issue_type', 'status')
    search_fields = ('location', 'description')
    readonly_fields = ('citizen', 'created_at')
    fields = ('description', 'issue_type', 'location', 'image', 'worker', 'status', 'citizen', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.citizen:
            obj.citizen = request.user
        super().save_model(request, obj, form, change)