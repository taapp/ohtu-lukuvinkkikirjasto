from database_connection import get_database_connection

def create_int_generator(i_start=0):
    i = i_start
    while True:
        yield i
        i += 1

generator_user_id = create_int_generator()
generator_vinkki_id = create_int_generator()

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists vinkit;
    ''')
    connection.commit()


def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        );
    ''')
    connection.commit()


def create_vinkit_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table vinkit (
            tyyppi TEXT,
            otsikko TEXT,
            kirjailija TEXT,
            isbn TEXT,
            tagit TEXT,
            url TEXT,
            kommentti TEXT,
            kuvaus TEXT,
            kurssit TEXT,
            luettu INTEGER
        );
    ''')
    connection.commit()


def create_tables(connection):
    create_users_table(connection)
    create_vinkit_table(connection)


def insert_default_data(connection):
    cursor = connection.cursor()
    sql_users = """INSERT INTO users(id, name, password) VALUES (?,?,?)"""
    cursor.execute(
        sql_users, [next(generator_user_id), "user", "passu"])
    sql_vinkit = 'insert into vinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql_vinkit, ["kirja", "Sinuhe Egyptiläinen", "Mika Waltari", "11111-22222", "","","Yksi lempikirjoistani!","","",""])
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    insert_default_data(connection)


if __name__ == "__main__":
    initialize_database()