from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('dashboard', views.DashboardViewSet, basename='dashboard')
router.register('games', views.GameViewSet, basename='games')
router.register('players', views.PlayerViewSet, basename='players')


urlpatterns = [
    path('latest_game_form/', views.latest_game_form, name='latest_game_form'),
    path('games/<int:pk>/', views.game_details, name='game_details'),
    path('players/<int:pk>/', views.player_details, name='player_details'),
]
