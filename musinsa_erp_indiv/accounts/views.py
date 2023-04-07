from django.shortcuts import render, redirect
from .models import UserModel

# Create your views here.


def sign_up_view(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html")
    elif request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, 'accounts/signup.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.email = email
            new_user.save()

        return redirect('/sign-in')


def sign_in_view(request):
    return render(request, "accounts/signin.html")
