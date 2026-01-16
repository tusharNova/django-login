from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from .models import *
from django.contrib import messages


def home(requests):
    return render(requests, "home.html")

def login(requests):
    if requests.mothod == 'POST':
        username = requests.POST.get('username')
        password = requests.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(requests, "User does not exist")
            return redirect('/login/')
        
        user = authenticate(requests, username=username, password=password)

        if user is None:
            messages.error(requests , "Invalid password")
            return redirect('/login/')
        else:
            login(requests, user)
            return redirect('/')
        
    return render(requests, "login.html")



def register(requests):
    if requests.method == "POST":
        first_name = requests.POST.get('first_name')
        last_name = requests.POST.get('last_name')
        username = requests.POST.get('username')
        password = requests.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(requests, "Username already taken")
            return redirect('/register/')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()

        messages.success(requests, "User registered successfully")
        return redirect('/login/')
    
    return render(requests, "register.html")