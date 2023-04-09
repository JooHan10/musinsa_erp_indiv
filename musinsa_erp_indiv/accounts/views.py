from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def sign_up_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, "accounts/signup.html")
    elif request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, 'accounts/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, "accounts/signup.html")
            else:
                UserModel.objects.create_user(
                    username=username, password=password, email=email)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # authenticate 함수는 암호화된 비밀번호와 현재 입력된 비밀번호가 일치하는지 & 그게 사용자와 일치하는지까지 한번에 확인시켜 줍니다.
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')
    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, "accounts/signin.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
