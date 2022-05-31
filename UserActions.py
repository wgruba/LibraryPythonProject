from tkinter.ttk import Label, Entry, Checkbutton, Button
import sqlite3
import tkinter as tk
from tkinter import END
import main as main
import Login
from User import User


class UserActions(tk.Frame):
    User = None
    def __init__(self, master):
        frame = tk.Frame.__init__(self, master)
        Label(self, text="User GUI").grid(row=1, column=1)
        Button(self, text="Return to start page",command=lambda: master.switch_frame(main.StartPage)).grid(row=4, column=2)


    def LoadUser(self):
        connection = sqlite3.connect('Library_dataBase.db')
        coursor = connection.cursor()
        userlogin = Login.LogedUser
        coursor.execute("SELECT *  FROM users WHERE login = " + userlogin)
        usersData = coursor.fetchall()
        for user in usersData:
            self.User = User(user[0],user[1],user[2])
        connection.commit()
        connection.close()

