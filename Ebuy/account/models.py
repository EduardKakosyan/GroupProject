from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

def generateUUID():
    return str(uuid4())

class Order(models.Model):
    complete = models.BooleanField(default=False, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
class Product(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="products")
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to="static/images")
    id = models.CharField(primary_key=True, default=generateUUID, max_length=36, unique=True, editable=False)
    
    def _str_(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ShippingAddress(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    
    def _str_(self):
        return str(self.id)