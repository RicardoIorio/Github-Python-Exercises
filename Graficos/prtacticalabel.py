from tkinter import *

raiz=Tk()

raiz.title("El Dolan")

frame=Frame(raiz,width=500,height=500)
frame.pack()

imagen=PhotoImage(file="dolan.jpg")

Label(frame, image=imagen).place(x=100,y=100)

raiz.mainloop()