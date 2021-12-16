import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_users()
        self.user_1 = User("user1","password1")
        self.vinkki_2 = User("user2","password2")


    def test_create(self):
        user_repository.create(self.user_1)
        user_loaded = user_repository.find_username("user1")
        self.assertEqual(user_loaded.password, "password1")

    def test_delete(self):
        user_repository.create(self.user_1)
        user_repository.delete("user1")
        self.assertIsNone(user_repository.find_username("user1"))

    def test_find_username(self):
        user_repository.create(self.user_1)
        user_found = user_repository.find_username("user1")
        self.assertEqual("user1", user_found.username)


    def test_delete_users(self):
        user_repository.create(self.user_1)
        user_repository.delete_users()
        user_loaded = user_repository.find_username("user1")
        self.assertEqual(user_loaded, None)
