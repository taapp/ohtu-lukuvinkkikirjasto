from flask_login import UserMixin

class Users(UserMixin):
    # Luodaan näennäinen tietokanta käyttäjistä
    user_database = {"kayttaja": ("kayttaja", "salasana"),
    "tunnus": ("tunnus", "passu")}

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    @classmethod
    def get_password(cls, username):
        username, password = cls.user_database.get(username)
        return password

    @classmethod
    def get_username(cls, username):
        username, password = cls.user_database.get(username)
        return username

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def roles(self):
        return ["ADMIN", "USER"]

    @classmethod
    def get(cls, id):
        return cls.user_database.get(id)

    def __str__(self):
        return f"id: {self.id}, username: {self.username}, password: {self.password}"