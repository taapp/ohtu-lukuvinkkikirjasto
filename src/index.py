from app import app
from lukuvinkki import Lukuvinkki
from lukuvinkkilista import Lukuvinkkilista


if __name__ == '__main__':

    #testataan, että lukuvinkki ja -lista toimii:
    vinkkilista = Lukuvinkkilista()
    vinkkilista.lisaa(Lukuvinkki("kirja", "Kirjan nimi tässä", "Kalle Kirjailija", "11111"))
    vinkkilista.lisaa(Lukuvinkki("podcast", "Podcastin nimi tässä", "Pertti Podaaja", url="www.osoite.fi", tagit="verkot, lifestyle, sijoittaminen"))
    vinkkilista.listaa()

    #käynnistää web-sovelluksen localhostille:
    app.run()
