from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import UserLoginForm, UserRegisterForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Success')
            return redirect('manuals')
        else:
            messages.error(request, 'Error')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login_app/login.html', context=context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success')
            return redirect('manuals')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'login_app/register.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('login')
