import unittest

from repositories.lukuvinkki_repository import lukuvinkki_repository
from entities.lukuvinkki import Lukuvinkki


class TestLukuvinkkiRepository(unittest.TestCase):
    def setUp(self):
        lukuvinkki_repository.poista_vinkit()
        self.vinkki_1 = Lukuvinkki(
            "podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen")
        self.vinkki_2 = Lukuvinkki(
            "kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111")

    def test_create(self):
        lukuvinkki_repository.create(self.vinkki_1)
        vinkit = lukuvinkki_repository.hae_vinkit()
        self.assertEqual(vinkit[0].__str__(), "Podcastin nimi tässä, kirjailija: Pertti Podaaja, ISBN: None, URL: www.osoite.fi, tagit: verkot, lifestyle, sijoittaminen, kuvaus: None, kommentit: None, luettu: 0, username: None")

