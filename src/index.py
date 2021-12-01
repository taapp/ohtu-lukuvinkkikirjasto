from app import app
from lukuvinkki import Lukuvinkki


if __name__ == '__main__':
    vinkki = Lukuvinkki("kirja", "Kalle Kirjailija", "11111")
    print(vinkki)
    app.run()
