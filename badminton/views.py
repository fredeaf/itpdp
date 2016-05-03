from django.shortcuts import render


def index(request):
    return render(request, 'template.html')


def hexminton(request):
    return render(request, 'hexminton.html')