class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def roles(self):
        return ["ADMIN", "USER"]

    def is_active(self):
        return True

    def __str__(self):
        return f"username: {self.username}"
