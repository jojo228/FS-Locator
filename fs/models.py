from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True, blank=True)
    prenom = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=200, null=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom


    
class Client(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    nom_client = models.CharField(max_length=200, null=True)
    Prénoms_client = models.CharField(max_length=200, null=True)
    zone = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200,  blank=True)
    latitude = models.CharField(max_length=200,  blank=True)
    date_creation = models.DateField(auto_now=True)         

    def __str__(self):
        return self.nom_client
    


    

