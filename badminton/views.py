from django.shortcuts import render

from .models import User


def index(request):
    return render(request, 'template.html')


def hexminton(request):
    count = User.objects.all().count()
    context ={
        'count': count,
    }
    return render(request, 'hexminton.html', context)
