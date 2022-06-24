import datetime

from django.test import TestCase

from plugin.models import Tache, Utilisateur


class TacheTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_label_champ_nom_tache(self):
        """Teste le label nom géneré par Django"""
        tache = Tache.objects.get(id=1)
        nom = tache._meta.get_field('nom_tache').verbose_name
        self.assertEqual(nom, 'nom tache')

    def test_label_champ_date_tache(self):
        """Teste le label date généré par Django"""
        tache = Tache.objects.get(id=1)
        nom = tache._meta.get_field('date').verbose_name
        self.assertEqual(nom, 'date')

    def test_label_champ_duree_tache(self):
        """Teste le label duree généré par Django"""
        tache = Tache.objects.get(id=1)
        nom = tache._meta.get_field('duree').verbose_name
        self.assertEqual(nom, 'duree')

    def test_taille_max_nom_tache(self):
        tache = Tache.objects.get(id=1)
        taille_max = tache._meta.get_field('nom_tache').max_length
        self.assertEqual(taille_max, 100)

    def test_string_tache(self):
        tache = Tache.objects.get(id=1)
        string_attendu = f'Nom de la tâche : {tache.nom_tache} | Date : {tache.date}'
        self.assertEqual(string_attendu, str(tache))

    def test_afficher_par_date_tache(self):
        tache_1 = Tache.objects.get(id=1)
        tache_2 = Tache.objects.get(id=2)
        tache_3 = Tache.objects.get(id=3)
        tache_4 = Tache.objects.get(id=4)
        liste_des_taches = [Tache.objects.get(id=5), Tache.objects.get(id=6), Tache.objects.get(id=7),
                            Tache.objects.get(id=8)]

        self.assertEqual(list(Tache.get_par_date(2019, 5)), [tache_1])
        self.assertEqual(list(Tache.get_par_date(2020, 10)), [tache_2])
        self.assertEqual(list(Tache.get_par_date(2025, 11)), [tache_3])
        self.assertEqual(list(Tache.get_par_date(2021, 2)), [tache_4])
        self.assertEqual(list(Tache.get_par_date(2022, 12)), liste_des_taches)

    def test_total_mensuel_en_secondes(self):
        self.assertEqual(Tache.total_mensuel_secondes(2019, 5), 172800)
        self.assertEqual(Tache.total_mensuel_secondes(2020, 10), 36000)
        self.assertEqual(Tache.total_mensuel_secondes(2025, 11), 29800)
        self.assertEqual(Tache.total_mensuel_secondes(2021, 2), 15840)
        self.assertEqual(Tache.total_mensuel_secondes(2022, 12), 2364420)

    def test_total_mensuel_formatter(self):
        self.assertEqual(Tache.total_mensuel_formatter(2019, 5), {'Jours': 2, 'Heures': 0, 'Minutes': 0})
        self.assertEqual(Tache.total_mensuel_formatter(2020, 10), {'Jours': 0, 'Heures': 10, 'Minutes': 0})
        self.assertEqual(Tache.total_mensuel_formatter(2025, 11), {'Jours': 0, 'Heures': 8, 'Minutes': 16})
        self.assertEqual(Tache.total_mensuel_formatter(2021, 2), {'Jours': 0, 'Heures': 4, 'Minutes': 24})
        self.assertEqual(Tache.total_mensuel_formatter(2022, 12), {'Jours': 27, 'Heures': 8, 'Minutes': 47})

    def test_duree_tache(self):
        tache_1 = Tache.objects.get(id=1)
        tache_2 = Tache.objects.get(id=2)
        tache_3 = Tache.objects.get(id=3)
        tache_4 = Tache.objects.get(id=4)
        tache_5 = Tache.objects.get(id=5)
        tache_6 = Tache.objects.get(id=6)
        tache_7 = Tache.objects.get(id=7)
        tache_8 = Tache.objects.get(id=8)

        self.assertEqual(tache_1.duree_tache(), '2 Jours : 0 Heure : 0 Minute')
        self.assertEqual(tache_2.duree_tache(), '0 Jour : 10 Heures : 0 Minute')
        self.assertEqual(tache_3.duree_tache(), '0 Jour : 8 Heures : 16 Minutes')
        self.assertEqual(tache_4.duree_tache(), '0 Jour : 4 Heures : 24 Minutes')
        self.assertEqual(tache_5.duree_tache(), '20 Jours : 11 Heures : 54 Minutes')
        self.assertEqual(tache_6.duree_tache(), '0 Jour : 20 Heures : 0 Minute')
        self.assertEqual(tache_7.duree_tache(), '0 Jour : 0 Heure : 43 Minutes')
        self.assertEqual(tache_8.duree_tache(), '6 Jours : 0 Heure : 10 Minutes')


class UtilisateurTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        d = datetime.timedelta(days=1, seconds=68400)
        Tache.objects.create(nom_tache='Tache 1', date='2019-05-20', duree=d)
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')

    def test_label_champ_nom_utilisateur(self):
        """Teste le label nom généré par Django"""
        utilisateur = Utilisateur.objects.get(id=1)
        nom = utilisateur._meta.get_field('nom').verbose_name
        self.assertEqual(nom, 'nom')

    def test_label_champ_prenom_utilisateur(self):
        """Teste le label prenom généré par Django"""
        utilisateur = Utilisateur.objects.get(id=1)
        prenom = utilisateur._meta.get_field('prenom').verbose_name
        self.assertEqual(prenom, 'prenom')

    def test_label_champ_mot_de_passe_utilisateur(self):
        """Teste le label mot de passe généré par Django"""
        utilisateur = Utilisateur.objects.get(id=1)
        mdp = utilisateur._meta.get_field('mot_de_passe').verbose_name
        self.assertEqual(mdp, 'mot de passe')

    def test_label_tache_utilisateur(self):
        """Teste le label tache généré par Django"""
        utilisateur = Utilisateur.objects.get(id=1)
        mdp = utilisateur._meta.get_field('tache').verbose_name
        self.assertEqual(mdp, 'tache')

    def test_taille_max_nom_utilisateur(self):
        utilisateur = Utilisateur.objects.get(id=1)
        taille_max = utilisateur._meta.get_field('nom').max_length
        self.assertEqual(taille_max, 20)

    def test_taille_max_prenom_utilisateur(self):
        utilisateur = Utilisateur.objects.get(id=1)
        taille_max = utilisateur._meta.get_field('prenom').max_length
        self.assertEqual(taille_max, 50)

    def test_taille_max_mot_de_passe_utilisateur(self):
        utilisateur = Utilisateur.objects.get(id=1)
        taille_max = utilisateur._meta.get_field('mot_de_passe').max_length
        self.assertEqual(taille_max, 50)

    def test_string_utilisateur(self):
        utilisateur = Utilisateur.objects.get(id=1)
        string_attendu = f'Utilisateur : {utilisateur.prenom} {utilisateur.nom}'
        self.assertEqual(string_attendu, str(utilisateur))
