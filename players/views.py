from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def latestGame(request):
    return render(request, 'players/latest_game.html')
