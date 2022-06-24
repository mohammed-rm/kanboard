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

    @staticmethod
    def get_par_date(annee: int, mois: int) -> QuerySet:
        """Récupération des taches appartenant à une même période (année, mois)"""
        return Tache.objects.filter(date__year=annee, date__month=mois)

    @staticmethod
    def total_mensuel_secondes(annee: int, mois: int) -> float:
        """Duree totale d'un ensemble de taches de la même année et du même mois en secondes"""
        result = datetime.timedelta()
        taches = Tache.get_par_date(annee, mois)
        for tache in taches:
            result += tache.duree
        return result.total_seconds()

    @staticmethod
    def total_mensuel_formatter(annee: int, mois: int) -> dict[str, int]:
        """Duree totale d'un ensemble de taches de la même année et du même mois"""
        total_secondes = datetime.timedelta(seconds=Tache.total_mensuel_secondes(annee, mois))
        result = datetime.timedelta() + total_secondes
        return dict(Jours=result.days, Heures=result.seconds // 3600, Minutes=(result.seconds // 60) % 60)

    def duree_tache(self):
        """Duree totale d'une seule tache"""
        jours_str, heures_str, minutes_str = "Jour", "Heure", "Minute"
        jours = self.duree.days
        secondes = self.duree.seconds

        minutes = secondes // 60
        heures = minutes // 60
        minutes = minutes % 60

        if jours > 1:
            jours_str = "Jours"
        if heures > 1:
            heures_str = "Heures"
        if minutes > 1:
            minutes_str = "Minutes"

        result = f'{jours} {jours_str} : {heures} {heures_str} : {minutes} {minutes_str}'

        return result

    @staticmethod
    def conversion_annee(annee):
        annee_str = ""
        for nombre in range(4):
            annee_str += annee[nombre]

        result = int(annee_str)

        return result

    @staticmethod
    def conversion_mois(mois):
        mois_str, mois_final_str = "", ""

        for nombre in range(5, 7):
            mois_str += mois[nombre]

        if mois_str[0] == '0':
            mois_final_str = mois_str[1]
        else:
            mois_final_str = mois_str
        result = int(mois_final_str)

        return result


class Utilisateur(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)
    tache = models.ManyToManyField(Tache)

    def __str__(self):
        return f'Utilisateur : {self.prenom} {self.nom}'
