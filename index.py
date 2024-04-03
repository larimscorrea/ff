from tkinter import *
from tkinter import messagebox

jan = Tk()
jan.title = "System - Acess Panel"
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

Logo = PhotoImage(file="/icons/Heaven_system-icon.png")

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raised")
LeftFrame.pack(side=LEFT)

LeftFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raised")
LeftFrame.pack(side=RIGHT)


jan.mainloop()
