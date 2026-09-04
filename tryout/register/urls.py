from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.home, name="register"),
    path("api/beneficiaries/", views.beneficiaries, name="beneficiaries"),
]
