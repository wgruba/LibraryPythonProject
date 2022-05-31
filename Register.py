import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import END
import main as main
from User import User
from tkinter.ttk import Label, Entry, Checkbutton, Button

class Register(tk.Frame):
    def __init__(self, master):
        frame = tk.Frame.__init__(self, master)
        Label(self, text="Registration").grid(row=1,column=1)
        Label(self,text="login").grid(row=2,column=1)
        Label(self, text="password").grid(row=3,column=1)
        login = Entry(self,width=30)
        login.grid(row=2,column=2)
        password = Entry(self,width=30)
        password.grid(row=3,column=2)
        ReturnButt = Button(self, text="Return to start page",command=lambda: master.switch_frame(main.StartPage)).grid(row=4,column=2)

        def RegisterUser(event = None):
            event = event
            connection = sqlite3.connect('Library_dataBase.db')
            coursor = connection.cursor()
            coursor.execute("SELECT * FROM users")
            logins = coursor.fetchall()
            UserExists = False
            for userData in logins:
                if userData[0] == login.get():
                    UserExists = True

            if UserExists:
                tk.messagebox.showinfo('Info', 'User with this login alredy exist!! Try Again')
            else:
                coursor.execute("INSERT INTO users VALUES (:login,:password,:ReadedBooks)",
                            {
                                'login': login.get(),
                                'password': password.get(),
                                'ReadedBooks': ''
                            }
                            )
                RegistredUser = User(login.get(), password.get())
                tk.messagebox.showinfo('Info', RegistredUser.login +' '+RegistredUser.password)
            login.delete(0, END)
            password.delete(0, END)
            connection.commit()
            connection.close()

        RegButt = Button(self, text= "Register", command=RegisterUser).grid(row=4, column=1)