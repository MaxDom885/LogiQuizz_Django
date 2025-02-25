from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Riddle(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    hint = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    time_taken = models.FloatField()
    date_played = models.DateTimeField(auto_now_add=True)
