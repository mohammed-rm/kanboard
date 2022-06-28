import datetime

from django.db import models
from django.db.models import QuerySet


# logique métier

class CRA:
    pass


class Tache(models.Model):
    nom_tache = models.CharField(max_length=100)
    date = models.DateField()
    duree = models.DurationField()

    def __str__(self):
        return f'Nom de la tâche : {self.nom_tache} | Date : {self.date}'


class Utilisateur(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)
    tache = models.ManyToManyField(Tache)

    def __str__(self):
        return f'Utilisateur : {self.prenom} {self.nom}'
