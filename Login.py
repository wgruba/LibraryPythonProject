import sqlite3
import tkinter as tk
import main as main
from tkinter import *
from UserActions import UserActions
from PIL import ImageTk,Image
import tkinter.messagebox

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global background_image
        background_image = ImageTk.PhotoImage(Image.open('pictures/lib.jpg').resize((3200,1100), Image.Resampling.LANCZOS))
        Canvas1 = tk.Canvas(self)
        Canvas1.create_image(300, 340, image=background_image)
        Canvas1.config(bg="white", width=700, height=800)
        Canvas1.pack(expand=True, fill='both')
        Label(self, text="login",bg='black', fg='white',font=('Courier', 15)).place(relx=0.15, rely=0.5, relwidth=0.15, relheight=0.1)
        Label(self, text="password",bg='black', fg='white',font=('Courier', 15)).place(relx=0.15, rely=0.6, relwidth=0.15, relheight=0.1)
        loginBut = Entry(self, width=30)
        loginBut.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        passwordBut = Entry(self, width=30,show='*')
        passwordBut.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        Button(self, text="Return to start page",bg='black', fg='white' ,command=lambda: master.switch_frame(main.StartPage)).place(relx=0.60,rely=0.85,relwidth=0.15,relheight=0.1)

        #function allowing to log user it to system
        def LoginUser():
            login = loginBut.get()
            password = passwordBut.get()
            connection = sqlite3.connect('Library_dataBase.db')
            coursor = connection.cursor()
            coursor.execute("SELECT * FROM users")
            logins = coursor.fetchall()
            success = False
            for userData in logins:
                if userData[0] == login and userData[1] == password:
                    tk.messagebox.showinfo('Info', 'Login Succesfull')
                    f = open("LogedUser.txt", "w")
                    f.write(login)
                    f.close()
                    success = True
            connection.commit()
            connection.close()
            if success:
                master.switch_frame(UserActions)
            else:
                self.LogedUser = None
                tk.messagebox.showinfo('Info', 'Login or Password is bad!! Try Again')
                loginBut.delete(0,END)
                passwordBut.delete(0, END)
        Button(self, text="Login",bg='black', fg='white' ,command=LoginUser).place(relx=0.15, rely=0.85, relwidth=0.15, relheight=0.1)



