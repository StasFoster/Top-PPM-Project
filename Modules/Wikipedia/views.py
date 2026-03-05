from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models


# Create your views here.
def add(request):
    s1 = models.Article()
    s1.title = "Stas"
    s1.disc = "asdfghjk"
    s1.save()
    print("asdfgh")
    return redirect("wiki_main")

def main(request):
    return render(request, "Wiki/index.html")

def api_art(request):
    s1 = models.Article.objects.all()[0]
    data = {
        "title" : s1.title,
        "disc" : s1.disc,
    }
    print("________1________")
    return JsonResponse(data)