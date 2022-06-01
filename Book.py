import sqlite3

class Book:
    name = ''
    author = ''
    nrPages = ''
    coverPage = ''
    readed = 0
    rating = 0

    def __init__(self,name,author,nrPages,coverPage, readed = 0, rating = 0):
        self.name = name
        self.author = author
        self.nrPages = nrPages
        self.coverPage = coverPage
        self.readed = readed
        self.rating = rating

    def SaveBook(self):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        coursor.execute("INSERT INTO books VALUES (:name,:author,:nrPages,:coverPage,:readed,:rating)",
                        {
                            'name': self.name,
                            'author': self.author,
                            'nrPages': self.nrPages,
                            'coverPage': self.coverPage,
                            'readed': self.readed,
                            'rating': self.rating
                        }
                        )
        connection.commit()
        connection.close()

    def UpdateBook(self):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        coursor.execute("""UPDATE books SET 
                     readed = :Readed,
                     rating = :Rating
                     WHERE name = :Name""",
                        {
                            'Name': self.name,
                            'Readed': self.readed,
                            'Rating': self.rating
                        })
        connection.commit()
        connection.close()

