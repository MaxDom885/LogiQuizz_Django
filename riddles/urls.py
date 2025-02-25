from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('categories/', views.category_list, name='category_list'),
    path('play/<int:category_id>/', views.play_riddle, name='play_riddle'),
    path('validate/<int:riddle_id>/', views.validate_answer, name='validate_answer'),
    path('hint/<int:riddle_id>/', views.request_hint, name='request_hint'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('reset/<int:category_id>/', views.reset_played_riddles, name='reset_played_riddles'),
     path('skip/<int:category_id>/', views.skip_riddle, name='skip_riddle'),  # Nouvelle URL pour passer
]