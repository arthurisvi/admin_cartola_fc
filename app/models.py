from django.db import models

# Create your models here.
class Footballer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class FootballerScore(models.Model):
    num_round = models.IntegerField()
    score = models.IntegerField()
    player = models.ForeignKey(Footballer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player.name