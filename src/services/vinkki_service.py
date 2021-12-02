from entities.lukuvinkki import Lukuvinkki
from entities.lukuvinkkilista import Lukuvinkkilista
from entities.user import User

class VinkkiService:
    def __init__(self):
        self.users = []

    def create_user(self, id, username, password):
        return User(id, username, password)
