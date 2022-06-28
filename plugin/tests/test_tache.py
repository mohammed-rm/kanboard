import datetime
from unittest import TestCase

from plugin.models import Tache


class TacheTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        d_1 = datetime.timedelta(days=2)
        Tache.objects.create(nom_tache='Tache 1', date='2019-05-20', duree=d_1)
        # create_tache_dao(tache)

    def test_create_tache_dao(self):
        self.assertEqual(1, Tache.objects.get(id=1))

    def test_delete_tache_dao(self):
        pass

    def test_get_par_date_dao(self):
        pass
