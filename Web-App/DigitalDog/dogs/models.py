from django.db import models


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    owner = models.ForeignKey("auth.User",on_delete=models.PROTECT,related_name="dogs")