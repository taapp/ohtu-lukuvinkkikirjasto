import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,

        }

        requests.post(f"{self._base_url}/register", data=data)

    def add_book(self, tyyppi, otsikko, kirjailija, isbn,
            tagit, url, kommentit, kuvaus, kurssit):
        data = {"tyyppi": tyyppi,
                "otsikko": otsikko,
                "kirjailija": kirjailija,
                "isbn": isbn,
                "tagit": tagit,
                "url": url,
                "kommentit": kommentit,
                "kuvaus": kuvaus,
                "kurssit": kurssit
        }

        requests.post(f"{self._base_url}/add_subject", data=data)
