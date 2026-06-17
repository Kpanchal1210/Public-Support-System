from django import forms
from django.core.exceptions import ValidationError
from PIL import Image

from .models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['issue_type', 'description', 'location', 'image']

        widgets = {
            'issue_type': forms.Select(attrs={'id': 'id_issue_type'}),
        }

    def clean_image(self):

        image = self.cleaned_data.get('image')

        if not image:
            return image

        # Max size: 5 MB
        if image.size > 5 * 1024 * 1024:
            raise ValidationError(
                "Image size must be less than 5 MB."
            )

        # Allowed image types
        allowed_types = [
            'image/jpeg',
            'image/jpg',
            'image/png'
        ]

        if image.content_type not in allowed_types:
            raise ValidationError(
                "Only JPG and PNG images are allowed."
            )

        # Verify it's a real image
        try:
            img = Image.open(image)
            img.verify()
        except Exception:
            raise ValidationError(
                "Invalid image file."
            )

        return image