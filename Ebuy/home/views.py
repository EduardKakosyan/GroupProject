from django.shortcuts import render
from account.models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    fields = {"products": products}
    return render(request, "home/index.html", fields)