from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Riddle(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hint = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question
    
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    time_taken = models.IntegerField()  # Temps en secondes
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.riddle.question}'
    

