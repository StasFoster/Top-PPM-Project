from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MyUser
from .forms import MyUserForm
from django.contrib.auth import login, logout
# from django.contrib.auth.models import User

def main(request):
    users = MyUser.objects.all()

    rec = []
    
    if request.user.is_authenticated:

        user = request.user

        my_vector = user.interests["vector"]

        for i in users:
            if request.user.id != i.id:
                i_vector = i.interests["vector"]
                
                a = 0
                for j in range(5):
                    a += (my_vector[j] * i_vector[j])

                b1 = 0
                for j in range(5):
                    b1 += my_vector[j] ** 2

                b2 = 0
                for j in range(5):
                    b2 += i_vector[j] ** 2

                b = b1 ** 0.5 + b2 ** 0.5

                scalar = a/b
                print(f"scalar {scalar}")
                if scalar >= 0.6:
                    rec.append(i)
                print(f"rec {rec}")

            

    data = {
            "users": rec,
            "user": request.user
    }
    return render(request, "Socnet/index.html", data)
        # return JsonResponse({"status":True})

def register(request):
    form = MyUserForm()
    return render(request, "Socnet/register.html", {"form":form})

def get_user_data(request):   
    form = MyUserForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request,user)

        list_interests = ["sport","video_game","book","films","automobile"]
        interests = {"vector":[]}
        for i in range(1, len(list_interests) + 1):
            interest = request.POST.get(list_interests[i - 1])
            if interest == "on":
                interests["vector"].append(1)
            else:
                interests["vector"].append(0)
        
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
    
def logout_user(request):
    logout(request)
    return redirect("socnet")

def profile(request, id):
    user = MyUser.objects.get(id=id)

    intrerests = {}
    for i, el in enumerate(["sport","video_game","book","films","automobile"], 0):
        intrerests[el] = user.interests["vector"][i]
    print(f"до {user.interests}")
    print(f"после {intrerests}")
    data = {
        "user": user,
        "interests": intrerests,
    }
    return render(request,"Socnet/user.html", data)