from entities.lukuvinkki import Lukuvinkki
from database_connection import get_database_connection

def get_vinkki_by_row(row):
    return Lukuvinkki(row["tyyppi"], row["otsikko"], row["kirjailija"], row["isbn"], row["tagit"],
        row["url"], row["kommentti"], row["kuvaus"], row["kurssit"], row["luettu"], row["username"]) if row else None

class LukuvinkkiRepository:
    def __init__(self, connection):
        self._connection = connection
        self.haku = "Sinuhe"
    
    def create(self, lukuvinkki):
        cursor = self._connection.cursor()
        print("LukuvinkkiRepository, create-metodi")
        cursor.execute(
            #'insert into lukuvinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            'insert into vinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu, username) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (lukuvinkki.tyyppi, lukuvinkki.otsikko, lukuvinkki.kirjailija, lukuvinkki.isbn, lukuvinkki.tagit, lukuvinkki.url, lukuvinkki.kommentti, lukuvinkki.kuvaus, lukuvinkki.kurssit, lukuvinkki.luettu, lukuvinkki.username)

        )

        self._connection.commit()

        return lukuvinkki

    def hae_vinkit(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from vinkit')

        rows = cursor.fetchall()

        return list(map(get_vinkki_by_row, rows))

    def hae_vinkkia(self, haku):
        cursor = self._connection.cursor()
        oikea_haku = f"%{haku}%"
        cursor.execute("SELECT * FROM vinkit WHERE otsikko LIKE ?", (oikea_haku,))

        rows = cursor.fetchall()

        return list(map(get_vinkki_by_row, rows))

    def palauta_vinkki(self, otsikko):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM vinkit WHERE otsikko = ?", (otsikko,))

        row = cursor.fetchall()

        return list(map(get_vinkki_by_row, row))

    #lukuvinkin muokkaus, ei vielä kokeiltu
    def muokkaa_vinkkia(self, vanhaotsikko, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit):
        cursor = self._connection.cursor()
        cursor.execute(
            'update vinkit set otsikko=?, kirjailija=?, isbn=?, tagit=?, url=?, kommentti=?, kuvaus=?, kurssit=? where otsikko = ?', 
            (otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, vanhaotsikko,)
            )

        self._connection.commit()

    def poista_vinkit(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from vinkit")
        self._connection.commit()

lukuvinkki_repository = LukuvinkkiRepository(get_database_connection())