from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
import json

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-account.html", {
        "profile": request.user
    })

def login_view(request):
    if request.method == "POST":
        # Access and authenticate user
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        #If user is returned, log in, else, return login page
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("account:index"))
        else:
            fields = {"message": "Invalid username or password, try again"}
            return render(request, "account/login.html", {
                "message": "Invalid email or password!"
            })
    return render(request, "account/login.html")

def logout_view(request):
    logout(request)
    return render(request, "account/login.html", {
        "message": "Logged out!"
    })

def register_view(request):
    form = UserCreateForm()
    
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created!")
            return render(request, "account/login.html", {
                "message": "User created!"
            })
        
    fields = {'form': form}
    return render(request, "account/register.html", fields)

def activity_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-activity.html", {
        "user": request.user
    })


def listings_view(request):
    form = ProductPosting()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    
    #Add new product
    if request.method == "POST":
        form = ProductPosting(request.POST, request.FILES)
        if form.is_valid():
            price = form.cleaned_data['price']
            name = form.cleaned_data['name']
            image = request.FILES['image']
            p = Product(user=request.user, price=price, name=name, image=image)
            p.save()
            messages.success(request, "Product created!")
            
            
    fields = {"user": request.user, "form": form}
    return render(request, "account/user-listings.html", fields)

#Remove product from user profile
def remove_product(request, id):
    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse("account:listings"))
    
def account_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-account.html", {
        "profile": request.user
    })

#Add products to cart
def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    request.user.order.products

def cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/cart.html")

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user
    
    
    return JsonResponse('productId', safe=False)