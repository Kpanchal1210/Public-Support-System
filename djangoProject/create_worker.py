import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create worker user
user, created = User.objects.get_or_create(
    username='worker1',
    defaults={'password': 'test123'}
)

# Create or update profile
profile, p_created = UserProfile.objects.get_or_create(
    user=user
)
profile.user_type = 'worker'
profile.save()

print(f'Worker created/updated: {user.username}')
print(f'Profile type: {profile.user_type}')

# Verify
print(f'\nTotal workers now: {User.objects.filter(userprofile__user_type="worker").count()}')
