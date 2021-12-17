from entities.lukuvinkki import Lukuvinkki
from entities.user import User

from repositories.lukuvinkki_repository import (
	lukuvinkki_repository as default_lukuvinkki_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class VinkkiService:
    def __init__(self, lukuvinkki_repository=default_lukuvinkki_repository, user_repository=default_user_repository):
        self._user = None
        self._lukuvinkki_repository = lukuvinkki_repository
        self._user_repository = user_repository

    def create_user(self, username, password):
        return User(username, password)
    
    def add_user_to_userlist(self, user):
        self._user_repository.create(user)

    def get_user(self, username):
        return self._user_repository.find_username(username)
    
    def create_vinkki(self, tyyppi, otsikko, kirjailija, isbn=None, tagit=None, url=None,
                        kommentti=None, kuvaus=None, kurssit=None, luettu=False, username=None):
        return Lukuvinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti,
                kuvaus, kurssit, luettu, username)

    def add_vinkki_to_vinkkilista(self, vinkki):
        self._lukuvinkki_repository.create(vinkki)

    def listaa_lukuvinkit(self):
        return self._lukuvinkki_repository.hae_vinkit()

    def muokkaa_vinkkia(self, vanhaotsikko, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit):
        self._lukuvinkki_repository.muokkaa_vinkkia(vanhaotsikko, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit)

    def palauta_lista(self):
        return self.listaa_lukuvinkit()

    def palauta_vinkki(self, otsikko):
        vinkki = self._lukuvinkki_repository.palauta_vinkki(otsikko)
        return vinkki

    def filter_by_user_current(self, vinkki_list):
        return [v for v in vinkki_list if v.username in (self._user.username, None)]

    def palauta_lista_user_current(self):
        if self._user is None:
            raise Exception("Yritetään palauttaa lista vaikka _user==None !")
        vinkit = self.listaa_lukuvinkit()
        return self.filter_by_user_current(vinkit)

    def hae_vinkkia(self, haku):
        return self._lukuvinkki_repository.hae_vinkkia(haku)

    def hae_vinkkia_user_current(self, haku):
        return self.filter_by_user_current(self.hae_vinkkia(haku))

vinkki_service = VinkkiService()
