from entities.lukuvinkki import Lukuvinkki
from entities.lukuvinkkilista import Lukuvinkkilista
from entities.user import User

from repositories.lukuvinkki_repository import (
	lukuvinkki_repository as default_lukuvinkki_repository
)

class VinkkiService:
    def __init__(self, lukuvinkki_repository=default_lukuvinkki_repository):
        self.users = []
        self.vinkkilista = Lukuvinkkilista()
        self._lukuvinkki_repository = lukuvinkki_repository

    def create_user(self, id, username, password):
        return User(id, username, password) # pylint: disable invalid-name

    def create_vinkki(self, tyyppi, otsikko, kirjailija, isbn=None, tagit=None, url=None,
                        kommentti=None, kuvaus=None, kurssit=None, luettu=False):

        return Lukuvinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti,
                kuvaus, kurssit, luettu)

    def add_vinkki_to_vinkkilista(self, vinkki):
        self.vinkkilista.lisaa(vinkki)

#    def listaa_vinkit(self):
#        self.vinkkilista.listaa()

    def listaa_lukuvinkit(self):
        return self._lukuvinkki_repository.hae_vinkit()

    def palauta_lista(self):
        return self.vinkkilista.palauta_lista()

vinkki_service = VinkkiService()
