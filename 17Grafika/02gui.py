from tkinter import *

window = Tk()
window.title("Pirmas kartas")
window.geometry("500x500")
# window.iconbitmap('pav.ico')

#ivestieslaikas
entry1 = Entry(window)
entry2 = Entry(window)

#laukas idedamas i langa
entry1.pack(pady=5)
entry2.pack(pady=5)

#mygtukai kuriam
button1 = Button(window, text='paspausk', command="")
button2 = Button(window, text='nespausk', command="")

button1.pack(pady=1)
button2.pack(pady=1)

window.mainloop()