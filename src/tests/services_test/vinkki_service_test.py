import unittest
from repositories import lukuvinkki_repository
from entities.user import User

from services.vinkki_service import vinkki_service, VinkkiService

class FakeLukuvinkkiRepository:
    def __init__(self) -> None:
        self.vinkit = []

    def create(self, lukuvinkki):
        self.vinkit.append(lukuvinkki)

    def hae_vinkit(self):
        return self.vinkit

    def hae_vinkkia(self, haku):
        return [v for v in self.vinkit if haku in v.otsikko]

class FakeUserRepository:
    def __init__(self) -> None:
        self.users = []

    def create(self, user):
        self.users.append(user)
        return user

    def find_username(self, username):
        user_ls = [u for u in self.users if u.username==username]
        return user_ls[0]


class TestVinkkiService(unittest.TestCase):
    def setUp(self) -> None:
        self.vinkki_service = VinkkiService(FakeLukuvinkkiRepository(), FakeUserRepository())
        self.vinkki_service._user = User("user", "password")
        self.vinkki_service._user_repository.users = [User("user", "password")]

    def test_create_user(self):
        user = self.vinkki_service.create_user('kalle', 'passu')
        self.assertEqual(user.__str__(), f"username: kalle")
        self.assertEqual(user.password, 'passu')

    def test_get_user(self):
        self.vinkki_service.add_user_to_userlist(self.vinkki_service.create_user('kalle', 'passu'))
        self.vinkki_service.add_user_to_userlist(self.vinkki_service.create_user('ville', 'salas'))
        user = self.vinkki_service.get_user('kalle')
        self.assertEqual(user.__str__(), f"username: kalle")
        self.assertEqual(user.password, 'passu')

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

    def test_palauta_lista_user_current(self):
        vinkki1 = self.vinkki_service.create_vinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen", username='user')
        vinkki2 = self.vinkki_service.create_vinkki("kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111")
        vinkki3 = self.vinkki_service.create_vinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen", username='user2')
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki1)
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki2)
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki3)
        vinkki_list = self.vinkki_service.palauta_lista_user_current()
        self.assertEqual(vinkki_list[0].__str__(), "Podcastin nimi tässä, kirjailija: Pertti Podaaja, ISBN: None, URL: www.osoite.fi, tagit: verkot, lifestyle, sijoittaminen, kuvaus: None, kommentit: None, luettu: False, username: user")
        self.assertEqual(vinkki_list[1].__str__(), "Kirjan nimi tässä, kirjailija: Kalle Kirjailija, ISBN: 11111, URL: None, tagit: None, kuvaus: None, kommentit: None, luettu: False, username: None")
        self.assertEqual(len(vinkki_list), 2)

    def test_hae_vinkkia(self):
        vinkki1 = self.vinkki_service.create_vinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen")
        vinkki2 = self.vinkki_service.create_vinkki("kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111")
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki1)
        self.vinkki_service.add_vinkki_to_vinkkilista(vinkki2)
        res = self.vinkki_service.hae_vinkkia('odcastin')
        self.assertEqual(res[0].__str__(), "Podcastin nimi tässä, kirjailija: Pertti Podaaja, ISBN: None, URL: www.osoite.fi, tagit: verkot, lifestyle, sijoittaminen, kuvaus: None, kommentit: None, luettu: False, username: None")
    
    