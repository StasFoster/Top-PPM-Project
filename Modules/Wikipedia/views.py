from django.shortcuts import render
from django.http import JsonResponse
from . import models


# Create your views here.
def add(request):
    s1 = models.Article()
    s1.title = "Stas"
    s1.disc = "asdfghjk"

def main(request):
    return render(request, "Wiki/imdex.html")

def api_art(request):
    s1 = models.Article.objects.get(title="Stas")
    data = {
        "title" : s1.title,
        "disc" : s1.disc,
    }
    return JsonResponse(data)