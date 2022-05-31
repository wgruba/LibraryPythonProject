from tkinter.ttk import Label, Entry, Checkbutton, Button
import sqlite3
import tkinter as tk
from tkinter import END
import main as main


class UserActions(tk.Frame):
    def __init__(self, master):
        frame = tk.Frame.__init__(self, master)
        Label(self, text="User GUI").grid(row=1, column=1)
        Button(self, text="Return to start page",command=lambda: master.switch_frame(main.StartPage)).grid(row=4, column=2)
