from tkinter import *
#issokantis langas
from tkinter import messagebox

def iterpimas():
    tekstas = entry1.get()
    sarasas.append(tekstas)
    list1.insert(0, tekstas)
    entry1.delete(0, END)

def salinimas():
    atsakymas = messagebox.askquestion("Ar tikrai nori pasalinti preke")
    if atsakymas == 'yes':
        for i in reversed(list1.curselection()):
            list1.delete(i)
            sarasas.remove(sarasas[i])
    pass

#langas
window = Tk()
window.title("Prekiu sarasas")
window.geometry("200x200")
window.iconbitmap("pav.ico")

#tekstas
label1 = Label(window, text='iterpk preke')
label1.grid(row=0, column=0, pady=5)

#mygtukas
button1 = Button(window, text='iterpkime...', command=iterpimas)
button1.grid(row=1, column=1)
button2 = Button(window, text='salinkime...', command=salinimas)
button2.grid(row=2, column=1)

#ivesties laukas
entry1 = Entry(window)
entry1.grid(column=0, row=1, padx=5)

#sarasas
sarasas = ["Kompas", "Mobiliakas", "Traskuciai", "Coca Cola", "Neribotas internetas"]
var = StringVar(value=sarasas)
list1 = Listbox(window, listvariable=var, selectmode="multiple")
list1.grid(column=0, row=2)

window.mainloop()