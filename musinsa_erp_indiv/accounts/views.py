from django.shortcuts import render
from . import models

# Create your views here.


def sign_up_view(request):
    return render(request, "accounts/signup.html")


def sign_in_view(request):
    return render(request, "accounts/signin.html")
