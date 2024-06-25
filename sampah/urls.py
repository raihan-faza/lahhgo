from django.urls import path
from . import views
urlpatterns = [
    path("", views.index_sampah, name="index"),
    path("details/", views.show_sampah, name="show_sampah"),
    path("create/", views.create_sampah, name="create_sampah"),
    path("update/", views.update_sampah, name="update_sampah"),
    path("buy/", views.create_transaction, name="create_transaction"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("products/", views.show_products, name="show_products"),
    path("upload3", views.upload3, name="upload3"),
    path("how-it-works", views.how_it_works, name="how-it-works"),
]
