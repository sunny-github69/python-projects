from tkinter import Tk
from tkinter.ttk import *
from time import strftime
import os
def shutdown():
    return os.system("shutdown /s /t 1")
def restart():
    return os.system("shutdown /r /t 1")
def logout():
    return os.system("shutdown -l")
murga = Tk()
murga.title('Power Control')
murga.geometry("500x500")
style = Style()
murga.resizable(True, True)

style.configure('W.TButton', font=('calibri', 40, 'bold'),
                foreground='black')
Button(murga, text="Shutdown", style='W.TButton',
       command=shutdown).place(x=100, y=100)
Button(murga, text="Restart", style='W.TButton',
       command=restart).place(x=100, y=180)
Button(murga, text="Log out", style='W.TButton',
       command=logout).place(x=100, y=260)
murga.mainloop()
