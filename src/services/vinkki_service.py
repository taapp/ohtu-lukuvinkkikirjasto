from entities.lukuvinkki import Lukuvinkki
from entities.lukuvinkkilista import Lukuvinkkilista
from entities.user import User

class VinkkiService:
    def __init__(self):
        self.users = []
        self.vinkkilista = Lukuvinkkilista()

    def create_user(self, id, username, password):
        return User(id, username, password)

    def create_vinkki(self, tyyppi, otsikko, kirjailija, isbn=None, tagit=None, url=None, kommentti=None, kuvaus=None, kurssit=None, luettu=False):
        return Lukuvinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu)

    def add_vinkki_to_vinkkilista(self, vinkki):
        self.vinkkilista.lisaa(vinkki)

    def listaa_vinkit(self):
        self.vinkkilista.listaa()

vinkki_service = VinkkiService()