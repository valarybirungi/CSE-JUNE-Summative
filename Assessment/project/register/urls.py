from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("register/", views.home, name="register"),
    path("register-list/", views.register_list, name="register_list"),
    path("api/beneficiaries/", views.beneficiaries, name="beneficiaries"),
]   