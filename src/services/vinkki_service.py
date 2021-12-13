from entities.lukuvinkki import Lukuvinkki
from entities.lukuvinkkilista import Lukuvinkkilista
from entities.user import User

from repositories.lukuvinkki_repository import (
	lukuvinkki_repository as default_lukuvinkki_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserInputError(Exception):
    pass

class ExistingUserError(Exception):
    pass

class VinkkiService:
    def __init__(self, lukuvinkki_repository=default_lukuvinkki_repository, user_repository=default_user_repository):
        self.users = []
        #self.vinkkilista = Lukuvinkkilista()
        self._user = None
        self._lukuvinkki_repository = lukuvinkki_repository
        self._user_repository = user_repository

    def create_user(self, username, password):
        return User(username, password)
    
    def add_user_to_userlist(self, user):
        self._user_repository.create(user)
    

    def create_vinkki(self, tyyppi, otsikko, kirjailija, isbn=None, tagit=None, url=None,
                        kommentti=None, kuvaus=None, kurssit=None, luettu=False):

        return Lukuvinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti,
                kuvaus, kurssit, luettu)

    def add_vinkki_to_vinkkilista(self, vinkki):
        #self.vinkkilista.lisaa(vinkki)
        self._lukuvinkki_repository.create(vinkki)

#    def listaa_vinkit(self):
#        self.vinkkilista.listaa()

    def listaa_lukuvinkit(self):
        return self._lukuvinkki_repository.hae_vinkit()

    def muokkaa_vinkkia(self, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit):
        self._lukuvinkki_repository.muokkaa_vinkkia(otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit)

    def palauta_lista(self):
        #return self.vinkkilista.palauta_lista()
        #return self._lukuvinkki_repository.hae_vinkit()
        return self.listaa_lukuvinkit()

vinkki_service = VinkkiService()
