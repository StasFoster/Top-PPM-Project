from django.urls import path
from . import views

urlpatterns = [
    path("wiki/main", views.main, name="wiki_main"),
    path("wiki/addArtikle", views.add, name="addArtikle"),
    path("wiki/api", views.api_art, name="Api_Artikle"),
]
