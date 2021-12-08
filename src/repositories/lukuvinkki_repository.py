from entities.lukuvinkki import Lukuvinkki
from database_connection import get_database_connection

class LukuvinkkiRepository:
    def __init__(self, connection):
        self._connection = connection

    
    def create(self, lukuvinkki):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into lukuvinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (lukuvinkki.tyyppi, lukuvinkki.otsikko, lukuvinkki.kirjailija, lukuvinkki.isbn, lukuvinkki.tagit, lukuvinkki.url, lukuvinkki.kommentti, lukuvinkki.kuvaus, lukuvinkki.kurssit, lukuvinkki.luettu)

        )

        self.connection.commit()

        return lukuvinkki


lukuvinkki_repository = LukuvinkkiRepository(get_database_connection())