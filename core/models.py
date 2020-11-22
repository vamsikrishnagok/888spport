from django.db import models

# Create your models here.

class Sport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)


class Selections(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    odds = models.FloatField()

class Markets(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    selections = models.ManyToManyField(Selections,related_name="markets")

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    markets = models.ManyToManyField(Markets)