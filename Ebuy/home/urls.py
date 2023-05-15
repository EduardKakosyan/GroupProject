#imports
from django.urls import path, include
from . import views

#application title
app_name = "home"

#application patterns for urls
urlpatterns = [
    path("", views.index, name = "index"),
    path("account/", include("account.urls"))
]