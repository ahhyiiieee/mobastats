from django.urls import path
from . import views

urlpatterns = [
    path('latest_game_form/', views.latest_game_form, name='latest_game_form'),
    path('games/<int:pk>/', views.game_details, name='game_details'),
    path('players/<int:pk>/', views.player_details, name='player_details'),
]