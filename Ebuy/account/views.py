from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user.html", {
        "user": request.user
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
            return render(request, "account/login.html", {
                "message": "Invalid email or password, try again"
            })
    return render(request, "account/login.html")

def logout_view(request):
    logout(request)
    return render(request, "account/login.html", {
        "message": "Logged out"
    })
    
def register_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        address = request.POST["address"]
        city = request.POST["city"]
        province = request.POST["province"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
        u = UserProfile(user=user, first_name=first_name, last_name=last_name,
                        address=address, city=city, province=province)
        u.save()
        return render(request, "account/login.html", {
            "message": "Account created, please log in"
        })
    return render(request, "account/register.html")

def activity_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-activity.html", {
        "user": request.user
    })
    
def messages_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-messages.html", {
        "user": request.user
    })
    
def account_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user-account.html", {
        "user": request.user
    })