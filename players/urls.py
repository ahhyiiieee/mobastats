from django.urls import path
from . import views

urlpatterns = [
    path('latest_game/', views.latestGame, name='latest_game'),
]