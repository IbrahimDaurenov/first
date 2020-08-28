from django.shortcuts import render
from .models import *


def index(request):
    context = dict()
    return render(request, 'komp/index.html', context)

def site(request):
    context = dict()
    return render(request, 'komp/site.html', context)

def types(request):
    context = dict()
    types = Type.objects.all()
    context['types'] = types
    return render(request, 'komp/types.html', context)

def game(request):
    context = dict()
    game = Nameofgame.objects.all()
    context['game'] = game
    return(request, 'komp/game.html', context)

def games(request):
    context = dict()
    games = Game.objects.all()
    context['games'] = games
    return render(request, 'komp/games.html', context)

def upgrade(request, key):
    context = dict()
    upgrade = Games.objects.get(pk = key)
    context['upgrade'] = upgrade

    if (request.method == "POST"):
        author = request.POST['author']
        content = request.POST['content']
        comment = Comment(author = author, content = content)
        comment.save()
        upgrade.comments.add(comment)
        upgrade.save()

    return render(request, 'komp/game.html', context)


# Create your views here.
