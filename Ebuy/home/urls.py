#imports
from django.urls import path
from . import views

#application title
app_name = "home"

#application patterns for urls
urlpatterns = [
    path("", views.index, name = "index")
]