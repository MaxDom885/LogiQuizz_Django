from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Crée un profil automatiquement lorsqu'un utilisateur est créé.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Sauvegarde le profil chaque fois que l'utilisateur est sauvegardé.
    """
    instance.profile.save()