from django.db.models import QuerySet

from plugin.models import Tache


def create_tache_dao(tache: Tache) -> None:
    tache.save()


def delete_tache_dao(pk: int) -> None:
    Tache.objects.get(id=pk).delete()


def get_par_date_dao(annee: int, mois: int) -> QuerySet:
    """Récupération des taches appartenant à une même période (année, mois)"""
    return Tache.objects.filter(date__year=annee, date__month=mois)
