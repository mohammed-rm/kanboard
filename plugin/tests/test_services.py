from django.test import TestCase

from plugin.logic.services import *
from plugin.models import Tache
from .data import create_test_data


class ServicesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_data()

    def test_get_par_date_tache(self):
        tache_1 = Tache.objects.get(id=1)
        tache_2 = Tache.objects.get(id=2)
        tache_3 = Tache.objects.get(id=3)
        tache_4 = Tache.objects.get(id=4)
        liste_des_taches = [Tache.objects.get(id=5), Tache.objects.get(id=6), Tache.objects.get(id=7),
                            Tache.objects.get(id=8)]

        self.assertEqual(list(get_par_date(2019, 5)), [tache_1])
        self.assertEqual(list(get_par_date(2020, 10)), [tache_2])
        self.assertEqual(list(get_par_date(2025, 11)), [tache_3])
        self.assertEqual(list(get_par_date(2021, 2)), [tache_4])
        self.assertEqual(list(get_par_date(2022, 12)), liste_des_taches)

    def test_total_mensuel_en_secondes(self):
        self.assertEqual(total_mensuel_secondes(2019, 5), 172800)
        self.assertEqual(total_mensuel_secondes(2020, 10), 36000)
        self.assertEqual(total_mensuel_secondes(2025, 11), 29800)
        self.assertEqual(total_mensuel_secondes(2021, 2), 15840)
        self.assertEqual(total_mensuel_secondes(2022, 12), 2364420)

    def test_total_mensuel_formatter(self):
        self.assertEqual(total_mensuel_formatter(2019, 5), {'Jours': 2, 'Heures': 0, 'Minutes': 0})
        self.assertEqual(total_mensuel_formatter(2020, 10), {'Jours': 0, 'Heures': 10, 'Minutes': 0})
        self.assertEqual(total_mensuel_formatter(2025, 11), {'Jours': 0, 'Heures': 8, 'Minutes': 16})
        self.assertEqual(total_mensuel_formatter(2021, 2), {'Jours': 0, 'Heures': 4, 'Minutes': 24})
        self.assertEqual(total_mensuel_formatter(2022, 12), {'Jours': 27, 'Heures': 8, 'Minutes': 47})

    def test_duree_tache(self):
        tache_1 = Tache.objects.get(id=1)
        tache_2 = Tache.objects.get(id=2)
        tache_3 = Tache.objects.get(id=3)
        tache_4 = Tache.objects.get(id=4)
        tache_5 = Tache.objects.get(id=5)
        tache_6 = Tache.objects.get(id=6)
        tache_7 = Tache.objects.get(id=7)
        tache_8 = Tache.objects.get(id=8)

        self.assertEqual(duree_tache(tache_1), '2 Jours : 0 Heure : 0 Minute')
        self.assertEqual(duree_tache(tache_2), '0 Jour : 10 Heures : 0 Minute')
        self.assertEqual(duree_tache(tache_3), '0 Jour : 8 Heures : 16 Minutes')
        self.assertEqual(duree_tache(tache_4), '0 Jour : 4 Heures : 24 Minutes')
        self.assertEqual(duree_tache(tache_5), '20 Jours : 11 Heures : 54 Minutes')
        self.assertEqual(duree_tache(tache_6), '0 Jour : 20 Heures : 0 Minute')
        self.assertEqual(duree_tache(tache_7), '0 Jour : 0 Heure : 43 Minutes')
        self.assertEqual(duree_tache(tache_8), '6 Jours : 0 Heure : 10 Minutes')

    def test_conversion_annee(self):
        date_1 = "2020-01"
        self.assertEqual(conversion_annee(date_1), 2020)

    def test_conversion_mois(self):
        date_1 = "2020-01"
        date_2 = "2020-10"

        self.assertEqual(conversion_mois(date_1), 1)
        self.assertEqual(conversion_mois(date_2), 10)
