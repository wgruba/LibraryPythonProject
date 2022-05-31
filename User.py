import sqlite3
import Book
import main as main

class User:
    login = ''
    password = ''
    ReadedBooks = {}
    def __init__(self,login,password):
        self.login = login
        self.password = password

    def saveUser(self):
        connection = sqlite3.connect('Library_dataBase.db')
        self.connection.close()

    def AddBookToAccount(self,Book):
        if Book.name != None and Book.name not in self.ReadedBooks.keys():
            self.ReadedBooks[Book.name] = (Book,False)
        else:
            print("something is bad!!!")

    def RateBook(self,Book,Rate):
        if Book.name in self.ReadedBooks.keys():
            Book.rating += Rate/10

    def SetAsReaded(self,Book):
        if Book.name in self.ReadedBooks.keys():
            Book.readed += 1
            self.ReadedBooks[Book.name] = (Book,True)

