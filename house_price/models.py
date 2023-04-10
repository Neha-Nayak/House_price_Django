from django.db import models

# Create your models here.
class Predict(models.Model):
    Location=models.CharField(max_length=300,primary_key=True)
    Area=models.IntegerField("max_length=30")
    Size=models.IntegerField("max_length=30")
    Bathroom=models.IntegerField("max_length=30")
    