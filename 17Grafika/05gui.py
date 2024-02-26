#isdestymas grid
from tkinter import *

window = Tk()
window.title("Pirmas kartas")
window.geometry("500x500")
# window.iconbitmap('pav.ico')

#ivestieslaikas
entry1 = Entry(window)
entry2 = Entry(window)

#laukas idedamas i langa
entry1.grid(row=0, column=0)
entry2.grid(row=2, column=2)

#mygtukai kuriam
button1 = Button(window, text='paspausk', command="")
button2 = Button(window, text='nespausk', command="")

button1.grid(row=1, column=1)
button2.grid(row=3, column=3)

window.mainloop()