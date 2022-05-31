import sqlite3
import tkinter as tk
from tkinter import END
import main as main
from tkinter.ttk import Label, Entry, Checkbutton, Button
from UserActions import UserActions

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        Label(self, text="Login").grid(row=1,column=1)
        Label(self, text="login").grid(row=2, column=1)
        Label(self, text="password").grid(row=3, column=1)
        loginBut = Entry(self, width=30)
        loginBut.grid(row=2, column=2)
        passwordBut = Entry(self, width=30)
        passwordBut.grid(row=3, column=2)
        ReturnButt = Button(self, text="Return to start page",command=lambda: master.switch_frame(main.StartPage)).grid(row=4,column=1)

        def LoginUser():
            login = loginBut.get()
            password = passwordBut.get()
            connection = sqlite3.connect('Library_dataBase.db')
            coursor = connection.cursor()
            coursor.execute("SELECT *, oid FROM users")
            logins = coursor.fetchall()
            success = False
            for userData in logins:
                if userData[0] == login and userData[1] == password:
                    tk.messagebox.showinfo('Info', 'Login Succesfull')
                    success = True
            connection.commit()
            connection.close()
            if success:
                master.switch_frame(UserActions)
            else:
                tk.messagebox.showinfo('Info', 'Login or Password is bad!! Try Again')
                loginBut.delete(0,END)
                passwordBut.delete(0, END)

        RegButt = Button(self, text="Login", command=LoginUser).grid(row=4, column=2)



