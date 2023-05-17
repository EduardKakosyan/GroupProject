from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages

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
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-listings.html", {
        "user": request.user
    })
    
def account_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-account.html", {
        "profile": request.user
    })

def cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/cart.html")
