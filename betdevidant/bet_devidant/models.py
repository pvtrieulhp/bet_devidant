from django.db import models

# Create your models here.


class Match(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    odds1 = models.DecimalField(max_digits=5, decimal_places=2)
    odds2 = models.DecimalField(max_digits=5, decimal_places=2)

