from tkinter import *

raiz=Tk()

raiz.title("Ventana de prueba")

raiz.resizable(1,1)

#raiz.iconbitmap("dolan.ico")

raiz.config(bg="blue")

raiz.config(bd=5)

raiz.config(relief="groove")

raiz.config(cursor="hand1")

frame=Frame()

frame.pack()

frame.config(bg="light blue")

frame.config(width="650",height="350")

frame.config(bd=45)

frame.config(relief="sunken")

raiz.mainloop()