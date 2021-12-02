import unittest

from services.vinkki_service import vinkki_service

class TestVinkkiService(unittest.TestCase):
    def test_create_user(self):
        user = vinkki_service.create_user(1, 'kalle', 'passu')
        self.assertEqual(user.__str__(), f"username: kalle, id: {1}")
        self.assertEqual(user.password, 'passu')

    def test_create_vinkki_podcast(self):
        vinkki = vinkki_service.create_vinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen")
        self.assertEqual(vinkki.__str__(), "Podcastin nimi tässä, kirjailija: Pertti Podaaja, ISBN: None, URL: www.osoite.fi, tagit: verkot, lifestyle, sijoittaminen, kuvaus: None, kommentit: None, luettu: False")

    def test_create_vinkki_kirja(self):
        vinkki = vinkki_service.create_vinkki("kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111")
        self.assertEqual(vinkki.__str__(), "Kirjan nimi tässä, kirjailija: Kalle Kirjailija, ISBN: 11111, URL: None, tagit: None, kuvaus: None, kommentit: None, luettu: False")
