from django.urls import path
from . import views

urlpatterns = [
    path('latest_game_form/', views.latest_game_form, name='latest_game_form'),
]