class Lukuvinkki:
    def __init__(self, tyyppi, otsikko, kirjailija, isbn=None, tagit=None, url=None, kommentti=None, kuvaus=None, kurssit=None, luettu=False, username=None):
        self.tyyppi = tyyppi
        self.otsikko = otsikko
        self.kirjailija = kirjailija
        self.isbn = isbn
        self.tagit = tagit
        self.url = url
        self.kommentti = kommentti
        self.kuvaus = kuvaus
        self.kurssit = kurssit
        self.luettu = luettu
        self.username = username

    def merkitse_luetuksi(self):
        self.luettu = True

    def __str__(self):
        return self.otsikko + ", kirjailija: " + self.kirjailija + ", ISBN: " + str(self.isbn) + ", URL: " + str(self.url) + ", tagit: " + str(self.tagit) + ", kuvaus: " + str(self.kuvaus) + ", kommentit: " + str(self.kommentti) + ", luettu: " + str(self.luettu) + ", username: " + str(self.username)