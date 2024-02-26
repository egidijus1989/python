#funcionalumas su grafika
from tkinter import *

window = Tk()
window.title("Pirmas kartas")
window.geometry("500x500")
# window.iconbitmap('pav.ico')

def pakeitimas():
    button1.config(font=('Comic Sans Ms', 10, "bold"))

#mygtukai kuriam
button1 = Button(window, text='paspausk', background="#dc143c", font=('Comic Sans Ms', 16, 'italic'), fg="green", activebackground="yellow", activeforeground="lime", command=pakeitimas, justify=CENTER)
button1.place(x=200, y=50)

window.mainloop()