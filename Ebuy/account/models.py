from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=1024)
    #Can be improved
    city = models.CharField(max_length=50, default="Halifax")
    province = models.CharField(max_length=2, default="NS")
    email = models.CharField(max_length=50, default="iamhandsome@gmail.com")
    
