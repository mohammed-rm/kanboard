import datetime
from unittest import TestCase

from plugin.models import Tache, Utilisateur


class TacheTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        d_1 = datetime.timedelta(days=2)
        Tache.objects.create(nom_tache='Tache 1', date='2019-05-20', duree=d_1)

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


class UtilisateurTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        d = datetime.timedelta(days=1, seconds=68400)
        Tache.objects.create(nom_tache='Tache 1', date='2019-05-20', duree=d)
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')

    def test_label_champ_nom_utilisateur(self):
        """Teste le label nom généré par Django"""
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        nom = utilisateur._meta.get_field('nom').verbose_name
        self.assertEqual(nom, 'nom')

    def test_label_champ_prenom_utilisateur(self):
        """Teste le label prenom généré par Django"""
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        prenom = utilisateur._meta.get_field('prenom').verbose_name
        self.assertEqual(prenom, 'prenom')

    def test_label_champ_mot_de_passe_utilisateur(self):
        """Teste le label mot de passe généré par Django"""
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        mdp = utilisateur._meta.get_field('mot_de_passe').verbose_name
        self.assertEqual(mdp, 'mot de passe')

    def test_label_tache_utilisateur(self):
        """Teste le label tache généré par Django"""
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        mdp = utilisateur._meta.get_field('tache').verbose_name
        self.assertEqual(mdp, 'tache')

    def test_taille_max_nom_utilisateur(self):
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        taille_max = utilisateur._meta.get_field('nom').max_length
        self.assertEqual(taille_max, 20)

    def test_taille_max_prenom_utilisateur(self):
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        taille_max = utilisateur._meta.get_field('prenom').max_length
        self.assertEqual(taille_max, 50)

    def test_taille_max_mot_de_passe_utilisateur(self):
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        taille_max = utilisateur._meta.get_field('mot_de_passe').max_length
        self.assertEqual(taille_max, 50)

    def test_string_utilisateur(self):
        Utilisateur.objects.create(nom='Lac', prenom='Jean', mot_de_passe='1234')
        utilisateur = Utilisateur.objects.get(id=1)
        string_attendu = f'Utilisateur : {utilisateur.prenom} {utilisateur.nom}'
        self.assertEqual(string_attendu, str(utilisateur))
