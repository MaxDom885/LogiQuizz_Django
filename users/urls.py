from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),  # URL pour la modification de profil
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),  
     path('logout/', auth_views.LogoutView.as_view(next_page='logout'), name='logout'),# Vue de déconnexion
     path('logout/', auth_views.LogoutView.as_view(template_name='templates/registration/logged_out.html'), name='logout'),
]