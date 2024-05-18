from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User


def userSignUp(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        if CustomUser.objects.filter(email=email).exists():
            return render(request, "sign_up.html", {"wrongEmail": "email already exits"})
        if password != confirmPassword:
            return render(request, "sign_up.html", {"wrongPassword": "incorrect password match"})
        user = CustomUser.objects.create_user(email=email, password=password)
        user.save()
        login(request, user)
        return redirect("/")
    return render(request, "sign_up.html")

def userLogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return render(request, "login.html", {"wrongEmailPassword": "wrong email or password"})
    return render(request, "login.html")


def userLogout(request):
    logout(request)