
import Login as login
import Register as register
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

# class representing main window
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        self.title('Library App')
        self.geometry("1000x600")
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relx=0,rely=0, relwidth=1, relheight=1)

# first page of application
class StartPage(tk.Frame):
    def __init__(self, master):
        global background_image
        frame = tk.Frame.__init__(self, master)
        #adding background
        background_image = ImageTk.PhotoImage(Image.open('pictures/lib.jpg').resize((1600,800),Image.Resampling.LANCZOS))
        Canvas1 = Canvas(self)
        Canvas1.create_image(300, 340, image=background_image)
        Canvas1.config(bg="white", width=700, height=800)
        Canvas1.pack(expand=True, fill='both')
        # adding some lables and buttons
        headingFrame1 = Frame(self, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to my Application", bg='black', fg='white',font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        tk.Button(self, text="login", bg='black', fg='white', command=lambda: master.switch_frame(login.Login)).place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
        tk.Button(self, text="register", bg='black', fg='white',command=lambda: master.switch_frame(register.Register)).place(relx=0.28, rely=0.5, relwidth=0.45,relheight=0.1)


#RUN!!!!!!!!!!!!!!
if __name__ == '__main__':
    window = SampleApp()
    window.mainloop()



