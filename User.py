import sqlite3
import Book
import main as main

class User:
    login = ''
    password = ''
    ReadedBooks = {}
    def __init__(self,login,password,ReadedBooksStr = None):
        self.login = login
        self.password = password
        if ReadedBooksStr == None:
            self.ReadedBooks = {}
        else:
            readedBooks = ReadedBooksStr.split('_')
            for book in readedBooks:
                self.loadBooks(book)

    def loadBooks(self,name):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        coursor.execute("SELECT * FROM books")
        booksData = coursor.fetchall()
        for book in booksData:
            if book[0] == name:
                book = Book(book[0],book[1],book[2],book[3],book[4],book[5])
                self.AddBookToAccount(book)

    def saveUser(self):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        coursor.execute("SELECT * FROM users WHERE login = " + self.login)
        usersData = coursor.fetchall()
        str = ''
        for key in self.ReadedBooks.keys():
            str += "_" + key
        for user in usersData:
            if user[0] == self.login:
                user[2] = str
        connection.commit()
        connection.close()

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

