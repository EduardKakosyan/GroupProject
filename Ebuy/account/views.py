from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account:login"))
    return render(request, "account/user.html")

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
    pass