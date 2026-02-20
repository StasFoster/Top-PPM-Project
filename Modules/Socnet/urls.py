from django.urls import path

from . import views

urlpatterns = [
    path("socnet/", views.main, name="socnet"),
    path("socnet/register/", views.register, name="register"),
]
