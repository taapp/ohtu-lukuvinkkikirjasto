import unittest

from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("user","password123")

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), self.user.username)

    def test_get_password(self):
        self.assertEqual(self.user.get_password(), self.user.password)

    def test_get_id(self):
        self.assertEqual(self.user.get_id(), self.user.username)

    def test_roles(self):
        roles = self.user.roles()
        self.assertEqual(roles[0], "ADMIN")
        self.assertEqual(roles[1], "USER")

    def test_is_active(self):
        self.assertEqual(self.user.is_active(), True)

    def test_is_authenticated(self):
        self.assertEqual(self.user.is_authenticated(), True)

    def test__str__(self):
        self.assertEqual(self.user.__str__(), f"username: {self.user.username}")
