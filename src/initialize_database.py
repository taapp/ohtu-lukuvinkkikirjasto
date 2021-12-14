from database_connection import get_database_connection

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
            luettu INTEGER,
            username TEXT
        );
    ''')
    connection.commit()


def create_tables(connection):
    create_users_table(connection)
    create_vinkit_table(connection)


def insert_default_data(connection):
    cursor = connection.cursor()
    sql_users = """INSERT INTO users(username, password) VALUES (?,?)"""
    cursor.execute(sql_users, ["tunnus", "passu"])
    cursor.execute(sql_users, ["kayttaja", "salasana"])
    sql_vinkit = 'insert into vinkit (tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, luettu, username) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql_vinkit, 
        ["kirja", "Sinuhe Egyptiläinen", "Mika Waltari", "11111-22222", "","","Yksi lempikirjoistani!","","","",None])
    cursor.execute(sql_vinkit, 
        ["video", "Merge sort algorithm", "", "", "","https://www.youtube.com/watch?v=TzeBrDU-JaY","Hyvä selitys merge sortin toiminnasta esimerkin avulla","","","","tunnus"])
    cursor.execute(sql_vinkit, 
        ["Podcast", "Jim Benson on Personal Kanban, Lean Coffee and collaboration", "Sami Honkonen", "", "Kanban, Lean Coffee","""Personal Kanban, which is an approach to dealing with the overload of stuff you need to deal with. 
  We dig into into its two simple rules, visualizing work and limiting work in progress. 
  We then walk through Lean Coffee, which is a simple and effective way to run your meetings.""","","TKT20006 Ohjelmistotuotanto","","","kayttaja"])
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    insert_default_data(connection)


if __name__ == "__main__":
    initialize_database()