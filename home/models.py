from django.db import models


# Create your models here.

class Addinfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    tech = models.CharField(max_length=30)
    loc1 = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    proj = models.CharField(max_length=50)
    blo1 = models.CharField(max_length=50)
    developer_rating = models.FloatField()
    score = models.FloatField()

   
    
def __str__(self):
    return self.name



