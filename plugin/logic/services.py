import datetime

from plugin.logic.tache import *


def create_tache(tache: Tache) -> None:
    create_tache_dao(tache)


def delete_tache(pk: int) -> None:
    delete_tache_dao(pk)


def get_par_date(annee: int, mois: int) -> QuerySet:
    return get_par_date_dao(annee, mois)


def total_mensuel_secondes(annee: int, mois: int) -> float:
    """Duree totale d'un ensemble de taches de la même année et du même mois en secondes"""
    result = datetime.timedelta()
    taches = get_par_date(annee, mois)
    for tache in taches:
        result += tache.duree
    return result.total_seconds()


def total_mensuel_formatter(annee: int, mois: int) -> dict[str, int]:
    """Duree totale d'un ensemble de taches de la même année et du même mois"""
    total_secondes = datetime.timedelta(seconds=total_mensuel_secondes(annee, mois))
    result = datetime.timedelta() + total_secondes
    return dict(Jours=result.days, Heures=result.seconds // 3600, Minutes=(result.seconds // 60) % 60)


def duree_tache(tache: Tache) -> str:
    """Duree totale d'une seule tache"""
    jours_str, heures_str, minutes_str = "Jour", "Heure", "Minute"
    jours = tache.duree.days
    secondes = tache.duree.seconds

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


def conversion_annee(annee: str) -> int:
    annee_str = ""
    for nombre in range(4):
        annee_str += annee[nombre]

    result = int(annee_str)

    return result


def conversion_mois(mois: str) -> int:
    mois_str, mois_final_str = "", ""

    for nombre in range(5, 7):
        mois_str += mois[nombre]

    if mois_str[0] == '0':
        mois_final_str = mois_str[1]
    else:
        mois_final_str = mois_str
    result = int(mois_final_str)
    return result
