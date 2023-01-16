from django.db import models
from django.contrib.auth.models import User
from account import UserProfile


# Create your models here.
class ProductProfile(models.Model):
    productName = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "product_profile")
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateTimeField()
    seller = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "user_profile")
