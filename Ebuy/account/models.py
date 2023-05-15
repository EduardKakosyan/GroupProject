from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    
    
    
