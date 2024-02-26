#koordinates
from tkinter import *

window = Tk()
window.title("Pirmas kartas")
window.geometry("500x500")
# window.iconbitmap('pav.ico')

#ivestieslaikas
entry1 = Entry(window)
entry2 = Entry(window)

#laukas idedamas i langa
entry1.place(x=50, y=50)
entry2.place(x=50, y=150)

#mygtukai kuriam
button1 = Button(window, text='paspausk', command="")
button2 = Button(window, text='nespausk', command="")

button1.place(x=200, y=50)
button2.place(x=200, y=150)

window.mainloop()