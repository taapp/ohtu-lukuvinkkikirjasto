from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserInputError(Exception):
    pass

class ExistingUserError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def create_user(self, username, password, password_confirmation):
        already_a_user = self._user_repository.find_username(username)
        if already_a_user:
            raise ExistingUserError(f"Tunnus on jo käytössä.")

        self.validate(username, password, password_confirmation)
        user = self._user_repository.create(
            User(username, password)
        )
        
        return user


    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Käyttäjätunnus tai salasana puuttuu")
        if password != password_confirmation:
            raise UserInputError("Salasanat eivät täsmää")

user_service = UserService()