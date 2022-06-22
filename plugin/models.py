from django.db import models


class Tache(models.Model):
    nom_tache = models.CharField(max_length=100)
    date = models.DateField()
    duree = models.DurationField()

    def __str__(self):
        return f'Nom de la tâche : {self.nom_tache} | Date : {self.date}'

    @staticmethod
    def afficher_par_date(annee: int, mois: int):
        return Tache.objects.filter(date__year=annee, date__month=mois)


class Utilisateur(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)
    tache = models.ManyToManyField(Tache)

    def __str__(self):
        return f'Utilisateur : {self.prenom} {self.nom}'
