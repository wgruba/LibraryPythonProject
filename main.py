import tkinter as tk
from PIL import ImageTk,Image

import DataBase
import Login as login
import Register as register



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=1,column=1)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label1 = tk.Label(self, text="This is the start page").grid(row=1,column=1)
        Butt1 = tk.Button(self, text="login",command=lambda: master.switch_frame(login.Login)).grid(row=2,column=1)
        Butt2 = tk.Button(self, text="register",command=lambda: master.switch_frame(register.Register)).grid(row=3,column=1)


if __name__ == '__main__':
    window = SampleApp()
    window.mainloop()



