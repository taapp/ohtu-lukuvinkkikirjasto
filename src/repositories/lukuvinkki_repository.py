from entities.lukuvinkki import Lukuvinkki
from database_connection import get_database_connection

def get_vinkki_by_row(row):
    return Lukuvinkki(row["tyyppi"], row["otsikko"], row["kirjailija"], row["isbn"], row["tagit"],
        row["url"], row["kommentti"], row["kuvaus"], row["kurssit"], row["luettu"]) if row else None

class LukuvinkkiRepository:
    def __init__(self, connection):
        self._connection = connection

    
    def create(self, lukuvinkki):
        cursor = self._connection.cursor()
        print("LukuvinkkiRepository, create-metodi")
        cursor.execute(
            #'insert into lukuvinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            'insert into vinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (lukuvinkki.tyyppi, lukuvinkki.otsikko, lukuvinkki.kirjailija, lukuvinkki.isbn, lukuvinkki.tagit, lukuvinkki.url, lukuvinkki.kommentti, lukuvinkki.kuvaus, lukuvinkki.kurssit, lukuvinkki.luettu)

        )

        self._connection.commit()

        return lukuvinkki

    def hae_vinkit(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from vinkit')

        rows = cursor.fetchall()

        return list(map(get_vinkki_by_row, rows))

    #lukuvinkin muokkaus, ei vielä kokeiltu
    def muokkaa_vinkkia(self, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit):
        cursor = self._connection.cursor()
        cursor.execute(
            'update vinkit set (otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit) values (?, ?, ?, ?, ?, ?, ?, ?)', 
            (otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit))

        self._connection.commit()


lukuvinkki_repository = LukuvinkkiRepository(get_database_connection())