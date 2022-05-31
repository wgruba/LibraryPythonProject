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
        self.connection.close()

