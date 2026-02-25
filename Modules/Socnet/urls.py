from django.urls import path

from . import views

urlpatterns = [
    path("socnet/", views.main, name="socnet"),
    path("socnet/register/", views.register, name="register"),
    path("socnet/get_user_data", views.get_user_data, name="get_user_data"),
    path("test_net", views.test),
]
