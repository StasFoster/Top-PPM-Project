from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MyUser
from .forms import MyUserForm
from django.contrib.auth import login, logout
# from django.contrib.auth.models import User

def main(request):
    users = MyUser.objects.all()

    data = {
        "users": users
    }
    return render(request, "Socnet/index.html", data)
    # return JsonResponse({"status":True})

def register(request):

    return render(request, "Socnet/register.html")

def get_user_data(request):   
    form = MyUserForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request,user)

        list_interests = ["sport","video_game","book","films","automobile"]
        interests = {}
        for i in range(1, len(list_interests) + 1):
            interest = request.POST.get(list_interests[i - 1])
            if interest == "on":
                interests[i] = 1
            else:
                interests[i] = 0
        
        user.interests = interests
        user.save()
    

    
    
    user = MyUser() # user = User()
    user.username = nickname
    user.first_name = username
    user.password = password
    user.interests = interests
    user.save()

    return redirect("socnet")




def test(request):
    if request.method == "POST":
        form = MyUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

    else:
        form = MyUserForm()
        return render(request, "Socnet/test.html", {"My_form": form})