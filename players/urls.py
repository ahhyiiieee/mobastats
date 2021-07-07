from django.urls import path
from . import views

urlpatterns = [
    path('latest_game_form/', views.latest_game_form, name='latest_game_form'),
    path('game_details/<int:pk>/', views.game_details, name='game_details'),
    path('player_details/<int:pk>/', views.player_details, name='player_details'),
]