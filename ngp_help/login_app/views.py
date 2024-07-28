from django.shortcuts import render, redirect
from django.contrib.auth import logout


def user_login(request):
    return render(request, 'login_app/login.html')


def user_register(request):
    return render(request, 'login_app/register.html')


def user_logout(request):
    logout(request)
    return redirect('login')
