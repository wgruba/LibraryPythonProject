import sqlite3
import Book

class User:
    login = ''
    password = ''
    ReadedBooks = {}
    def __init__(self,login,password,ReadedBooksStr = None):
        self.login = login
        self.password = password
        if ReadedBooksStr == None or ReadedBooksStr == '':
            self.ReadedBooks = {}
        else:
            readedBooks = ReadedBooksStr.split('_')
            for book in readedBooks:
                self.loadBooks(book)

    #loading books from data base to user
    def loadBooks(self,name):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        coursor.execute("SELECT * FROM books")
        booksData = coursor.fetchall()
        for book in booksData:
            if book[0] == name:
                TempBook = Book.Book(book[0],book[1],book[2],book[3],book[4],book[5])
                self.AddBookToAccount(TempBook)

    #updating User data in database
    def updateUser(self):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        str = ''
        for key in self.ReadedBooks.keys():
            str += key + "_"

        coursor.execute("""UPDATE users SET 
                ReadedBooks = :Books
                WHERE login = :login""",
                        {
                            'login': self.login,
                            'Books': str
                        })
        connection.commit()
        connection.close()

    #adding a new book to user account
    def AddBookToAccount(self,Book):
        if Book.name != None and Book.name not in self.ReadedBooks.keys():
            self.ReadedBooks[Book.name] = (Book,False)
        else:
            print('yes')

    #setting book as readed in user account
    def SetAsReaded(self,Book):
        if Book.name in self.ReadedBooks.keys():
            if not self.ReadedBooks[Book.name][1]:
                Book.readed += 1
                self.ReadedBooks[Book.name] = (Book,True)

