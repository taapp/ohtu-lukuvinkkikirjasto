import unittest
from repositories import lukuvinkki_repository

from services.vinkki_service import vinkki_service, VinkkiService

class FakeLukuvinkkiRepository:
    def __init__(self) -> None:
        self.vinkit = []

    def create(self, lukuvinkki):
        self.vinkit.append(lukuvinkki)
    
    def hae_vinkit(self):
        return self.vinkit

class TestVinkkiService(unittest.TestCase):
    def setUp(self) -> None:
        self.vinkki_service = VinkkiService(FakeLukuvinkkiRepository())

#    def test_create_user(self):
#        user = self.vinkki_service.create_user(1, 'kalle', 'passu')
#        self.assertEqual(user.__str__(), f"username: kalle, id: {1}")
#        self.assertEqual(user.password, 'passu')

    def test_create_vinkki_podcast(self):
        vinkki = self.vinkki_service.create_vinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen")
        self.assertEqual(vinkki.__str__(), "Podcastin nimi tässä, kirjailija: Pertti Podaaja, ISBN: None, URL: www.osoite.fi, tagit: verkot, lifestyle, sijoittaminen, kuvaus: None, kommentit: None, luettu: False, username: None")

    def test_create_vinkki_kirja(self):
        vinkki = self.vinkki_service.create_vinkki("kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111")
        self.assertEqual(vinkki.__str__(), "Kirjan nimi tässä, kirjailija: Kalle Kirjailija, ISBN: 11111, URL: None, tagit: None, kuvaus: None, kommentit: None, luettu: False, username: None")

    def test_palauta_lista(self):
        vinkki1 = self.vinkki_service.create_vinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen")
        vinkki2 = self.vinkki_service.create_vinkki("kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111")
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki1)
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki2)
        vinkki_list = self.vinkki_service.palauta_lista()
        self.assertEqual(vinkki_list[0].__str__(), "Podcastin nimi tässä, kirjailija: Pertti Podaaja, ISBN: None, URL: www.osoite.fi, tagit: verkot, lifestyle, sijoittaminen, kuvaus: None, kommentit: None, luettu: False, username: None")
        self.assertEqual(vinkki_list[1].__str__(), "Kirjan nimi tässä, kirjailija: Kalle Kirjailija, ISBN: 11111, URL: None, tagit: None, kuvaus: None, kommentit: None, luettu: False, username: None")
