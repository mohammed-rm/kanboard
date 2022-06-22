import datetime

from django.test import TestCase

from .models import Tache


class TacheTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        d = datetime.timedelta(days=-1, seconds=68400)
        Tache.objects.create(nom_tache='Tache 1', date='2019-05-20', duree=d)
        Tache.objects.create(nom_tache='Tache 2', date='2020-10-20', duree=d)
        Tache.objects.create(nom_tache='Tache 3', date='2025-11-20', duree=d)
        Tache.objects.create(nom_tache='Tache 4', date='2021-02-20', duree=d)

        Tache.objects.create(nom_tache='Tache 5', date='2022-12-20', duree=d)
        Tache.objects.create(nom_tache='Tache 6', date='2022-12-20', duree=d)
        Tache.objects.create(nom_tache='Tache 7', date='2022-12-20', duree=d)
        Tache.objects.create(nom_tache='Tache 8', date='2022-12-20', duree=d)

    def test_afficher_par_date(self):
        tache_1 = Tache.objects.get(id=1)
        tache_2 = Tache.objects.get(id=2)
        tache_3 = Tache.objects.get(id=3)
        tache_4 = Tache.objects.get(id=4)
        liste_des_taches = [Tache.objects.get(id=5), Tache.objects.get(id=6), Tache.objects.get(id=7),
                            Tache.objects.get(id=8)]

        self.assertEqual(list(Tache.afficher_par_date(2019, 5)), [tache_1])
        self.assertEqual(list(Tache.afficher_par_date(2020, 10)), [tache_2])
        self.assertEqual(list(Tache.afficher_par_date(2025, 11)), [tache_3])
        self.assertEqual(list(Tache.afficher_par_date(2021, 2)), [tache_4])
        self.assertEqual(list(Tache.afficher_par_date(2022, 12)), liste_des_taches)


class UtilisateurTestCase(TestCase):
    pass
