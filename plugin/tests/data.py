import datetime

from plugin.models import Tache


def create_test_data():
    d_1 = datetime.timedelta(days=2)
    d_2 = datetime.timedelta(hours=10)
    d_3 = datetime.timedelta(hours=8, seconds=1000)
    d_4 = datetime.timedelta(hours=4, minutes=24)

    d_5 = datetime.timedelta(days=20, hours=11, minutes=54)
    d_6 = datetime.timedelta(hours=20)
    d_7 = datetime.timedelta(minutes=43)
    d_8 = datetime.timedelta(days=6, minutes=10)

    Tache.objects.create(nom_tache='Tache 1', date='2019-05-20', duree=d_1)
    Tache.objects.create(nom_tache='Tache 2', date='2020-10-20', duree=d_2)
    Tache.objects.create(nom_tache='Tache 3', date='2025-11-20', duree=d_3)
    Tache.objects.create(nom_tache='Tache 4', date='2021-02-20', duree=d_4)

    Tache.objects.create(nom_tache='Tache 5', date='2022-12-01', duree=d_5)
    Tache.objects.create(nom_tache='Tache 6', date='2022-12-10', duree=d_6)
    Tache.objects.create(nom_tache='Tache 7', date='2022-12-19', duree=d_7)
    Tache.objects.create(nom_tache='Tache 8', date='2022-12-23', duree=d_8)
