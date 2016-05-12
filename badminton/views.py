from django.shortcuts import render

from .models import Player


def index(request):
    return render(request, 'contact.html')


def hexminton(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'base.html', context)


def player_details(request, player_id):
    context = {
        'player' : Player.objects.get(pk=player_id),
               }
    return render(request, 'players/detail.html', context)
