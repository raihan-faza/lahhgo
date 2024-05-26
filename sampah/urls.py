from django.urls import path
from . import views
urlpatterns = [
    path("", views.index_sampah, name="index_sampah"),
    path("details/", views.show_sampah, name="show_sampah"),
    path("create/", views.create_sampah, name="create_sampah"),
    path("update/", views.update_sampah, name="update_sampah"),
    path("buy/", views.create_transaction, name="create_transaction"),
    path("register/", views.register, name="register_user"),
    path("login/", views.login, name="login_user"),
]
