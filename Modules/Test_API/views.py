from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def test_api(request):
    data = {
        "name": "dffdf",
        "age": 20,
        "like_color": "white",
    }
    return JsonResponse(data)

def main(request):
    return render(request, "Test_API/index.html")