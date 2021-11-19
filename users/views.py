from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated: # the request object that gets passed in as part of the request for every user in django has a user attribute with an 'is_authenticated attirbute
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] # 'username' comes from input type field name in login.html
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) # authenticate is imported at top
        if user is not None: # user being 'not None' means authentication was successful
            login(request, user) # log in the user
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })