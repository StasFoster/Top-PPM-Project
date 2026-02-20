from django.shortcuts import render
from django.http import JsonResponse

def main(request):
    return render(request, "Socnet/index.html")
    # return JsonResponse({"status":True})

def register(request):
    return render(request, "Socnet/register.html")