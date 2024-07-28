from django.shortcuts import render


def q(request):
    return render(request, 'manual/manuals.html')
