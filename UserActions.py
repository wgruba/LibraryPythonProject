from tkinter.ttk import Label, Entry, Checkbutton, Button
import sqlite3
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import main as main
from Book import Book
from User import User


class UserActions(tk.Frame):
    User = None
    def __init__(self, master):
        frame = tk.Frame.__init__(self, master)
        Label(self, text="User GUI").grid(row=1, column=1)
        Button(self, text="LoadData", command= self.LoadUser).grid(row= 4,column=1)
        Button(self, text="Return to start page",command=lambda: master.switch_frame(main.StartPage)).grid(row=4, column=3)
        Button(self, text="Add some books", command=self.addSomeBooks).grid(row=4,column=4)
        BookNameBut = Entry(self,width=30)
        BookNameBut.grid(row=2,column=1)
        # Searching for chossen BookPulpit

        def SearchBook():
            global bookImage
            book = None
            bookName = BookNameBut.get()
            connection = sqlite3.connect('Library_dataBase.db')
            coursor = connection.cursor()
            coursor.execute("SELECT * FROM books")
            books = coursor.fetchall()
            for bookData in books:
                if bookData[0] == bookName:
                    book = bookData
            if book is not None:
                top = tk.Toplevel()
                bookImage = ImageTk.PhotoImage(Image.open(book[3]))
                image = Label(top,image=bookImage).grid(row=2,column=1)
                Label(top,text=book[0]).grid(row=1,column=1)
                Label(top,text=book[1]).grid(row=3,column=1)
                Label(top, text="" + str(book[2])+"str.").grid(row=4,column=1)
                Label(top, text="Readed: " + str(book[4]) + " times").grid(row=5, column=1)
                Label(top, text="Rating: " + str(book[5]) + "/10").grid(row=6, column=1)
                Button(top, text="Set as Readed", command= self.LoadUser).grid(row=7,column=1)
                Button(top, text="Add to Your Books", command=self.LoadUser).grid(row=7, column=2)
                Button(top, text="Rate", command=self.User).grid(row=7, column=3)
                Button(top, text="Exit", command=top.destroy).grid(row=7, column=4)
            else:
                tk.messagebox.showinfo('Info', 'There is no book with that title')
            connection.commit()
            connection.close()

        Button(self, text="BookSearching", command=SearchBook).grid(row=3, column=2)

    def SetAsReaded(self):
        pass

    def AddToUserBooks(self):
        pass

    def RateBook(self):
        pass



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

