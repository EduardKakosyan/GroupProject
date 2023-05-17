from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("activity/", views.activity_view, name="activity"),
    path("listings/", views.listings_view, name="listings"),
    path("info/", views.account_view, name="info"),
    path("cart/", views.cart, name="cart"),
    path("remove_product/<id>", views.remove_product, name="remove_product")
]