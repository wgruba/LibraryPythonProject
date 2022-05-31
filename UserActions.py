from tkinter.ttk import Label, Entry, Checkbutton, Button
import sqlite3
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import main as main
from Book import Book
from User import User


class UserActions(tk.Frame):
    book = None
    User = None
    def __init__(self, master):
        frame = tk.Frame.__init__(self, master)
        Label(self, text="User GUI").grid(row=1, column=1)
        Button(self, text="LoadData", command= self.LoadUser).grid(row= 4,column=1)
        Button(self, text="Return to start page",command=lambda: master.switch_frame(main.StartPage)).grid(row=4, column=3)
        Button(self, text="Add some books", command=self.addSomeBooks).grid(row=4,column=4)
        BookNameBut = Entry(self,width=30)
        BookNameBut.grid(row=2,column=1)

        def SearchBook():
            global bookImage
            bookName = BookNameBut.get()
            connection = sqlite3.connect('Library_dataBase.db')
            coursor = connection.cursor()
            coursor.execute("SELECT * FROM books")
            books = coursor.fetchall()
            for bookData in books:
                if bookData[0] == bookName:
                    self.book = Book(bookData[0],bookData[1],bookData[2],bookData[3],bookData[4],)
            if self.book is not None:
                top = tk.Toplevel()
                bookImage = ImageTk.PhotoImage(Image.open(self.book.coverPage))
                image = Label(top,image=bookImage).grid(row=2,column=1)
                Label(top,text=self.book.name).grid(row=1,column=1)
                Label(top,text=self.book.author).grid(row=3,column=1)
                Label(top, text="" + str(self.book.nrPages)+"str.").grid(row=4,column=1)
                Label(top, text="Readed: " + str(self.book.readed) + " times").grid(row=5, column=1)
                Label(top, text="Rating: " + str(self.book.rating) + "/10").grid(row=6, column=1)
                Button(top, text="Set as Readed", command= self.LoadUser).grid(row=7,column=1)
                Button(top, text="Add to Your Books", command=self.AddToUserBooks).grid(row=7, column=2)
                Button(top, text="Rate", command=self.rateBook).grid(row=7, column=3)
                Button(top, text="Exit", command=top.destroy).grid(row=7, column=4)
            else:
                tk.messagebox.showinfo('Info', 'There is no book with that title')
            connection.commit()
            connection.close()

        Button(self, text="BookSearching", command=SearchBook).grid(row=3, column=2)

    def SetAsReaded(self):
        pass

    def AddToUserBooks(self):
        if self.book.name != None and self.book.name not in self.User.ReadedBooks.keys():
            self.User.ReadedBooks[self.book.name] = (self.book,False)
            tk.messagebox.showinfo('Info', 'succesfully added' + self.User.ReadedBooks[self.book.name][0].name)
            self.User.saveUser()
        else:
            tk.messagebox.showinfo('Info', 'cannot add to Account')

    def rateBook(self):
        top2 = tk.Toplevel()
        Label(top2, text="How do you rate these book? (1-10)").grid(row=1, column=3)
        ratingEn = Entry(top2,width=30)
        ratingEn.grid(row=2,column=3)
        def inside():
            rate = int(ratingEn.get())
            if rate > 1 and rate < 10:
                self.book.rating += rate/10
                self.book.SaveBook()
            else:
                tk.messagebox.showinfo('Info', 'wrong rating')
        Button(top2, text="Rate", command=inside).grid(row=3, column=1)
        Button(top2, text="Exit", command=top2.destroy).grid(row=3, column=4)


    def addSomeBooks(self):
        book1 = Book('Cień i kość','Leigh Bardugo',288,'pictures/cień_i_kość.jpg')
        book2 = Book('Krew i miód', 'Shelby Mahurin', 512, 'pictures/krew_i_miód.png')
        book3 = Book('Mentalista', 'Henrik Fexeus', 680, 'pictures/mentalista.png')
        book4 = Book('Pan Tadeusz', 'Adam Mickiewicz', 344, 'pictures/pan_tadeusz.png')

        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        coursor.execute("SELECT * FROM books")
        adds = coursor.fetchall()
        UserExists = False
        for userData in adds:
            if userData[0] == book1.name:
                UserExists = True
        if UserExists:
            tk.messagebox.showinfo('Info', 'These books exist!! Try Again')
        else:
            book1.SaveBook()
            book2.SaveBook()
            book3.SaveBook()
            book4.SaveBook()

    def LoadUser(self):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        f = open("LogedUser.txt", "r")
        userlogin = f.readline()
        coursor.execute("SELECT *  FROM users ")
        usersData = coursor.fetchall()
        for user in usersData:
            if user[0] == userlogin:
                self.User = User(user[0],user[1],user[2])
        connection.commit()
        connection.close()

