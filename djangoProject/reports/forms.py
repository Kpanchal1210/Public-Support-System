from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_type', 'description', 'location', 'image']
        widgets = {
            'issue_type': forms.Select(attrs={'id': 'id_issue_type'}),
        }