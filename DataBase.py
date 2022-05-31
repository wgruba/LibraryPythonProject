import sqlite3

class DataBase():
    def __init__(self):
        self.connection = sqlite3.connect('Library_dataBase.db')
        self.coursor = self.connection.cursor()
        self.coursor.execute("""CREATE TABLE users (
                            login text,
                            password text
                                )""")
        self.coursor.execute("""CREATE TABLE books (
                                    name text,
                                    author text,
                                    nrPages integer,
                                    coverPage text,
                                    readed integer,
                                    rating real
                                        )""")
        self.connection.commit()
        self.connection.close()