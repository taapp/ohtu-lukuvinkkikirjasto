from database_connection import get_database_connection

class User:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"username: {self.username}, id: {self.id}"


def load_user(connection, username, password):
    cursor = connection.cursor()
    cursor.execute("SELECT id,name,password FROM users WHERE name=? AND password=?", [
                    username, password])
    res = cursor.fetchone()
    if res is not None:
        user = User(res[0], res[1], res[2])
        return user
    return None

def main():
    print("Hello world!")
    connection = get_database_connection()
    user = load_user(connection, 'user', 'passu')
    print(user)

if __name__ == '__main__':
    main()
