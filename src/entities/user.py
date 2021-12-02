class User:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"username: {self.username}, id: {self.id}"