from django.shortcuts import render


def q(request):
    return render(request, 'base.html')
