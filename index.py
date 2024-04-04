from tkinter import *
from tkinter import messagebox
from tkinter import ttk

jan = Tk()
jan.title = "System - Acess Panel"
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

logo = PhotoImage(file="icons/icon.png")
logo = Frame(width=100, height=100)

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raised")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=150, y=160)

jan.mainloop()
