from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'issue_type', 'location', 'image']
        widgets = {
            'category': forms.HiddenInput(),
        }