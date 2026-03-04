from django.urls import path
from . import views 

urlpatterns = [
    path("api_test/", views.test_api, name="api"),
    path("main_api/", views.main, name="main_api"),
]
