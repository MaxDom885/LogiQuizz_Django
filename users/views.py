from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige vers la page d'accueil si l'utilisateur est déjà connecté
    return auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True)(request)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_update(request):
    profile = request.user.profile  # Récupère le profil de l'utilisateur connecté
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers la page de profil après la mise à jour
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'users/profile_update.html', {'form': form})
