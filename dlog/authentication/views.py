from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import *


def home(requests):
    return render(requests, "authentication/home.html")

