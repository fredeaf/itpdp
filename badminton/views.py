from django.shortcuts import render

from .models import User


def index(request):
    return render(request, 'template.html')


def hexminton(request):
    count = User.objects.all().count()
    context ={
        'count': count,
    }
    request.session['location'] = "unknown"
    if request.user.is_authenticated():
        request.session['location'] = "earth"
    return render(request, 'base.html', context)
