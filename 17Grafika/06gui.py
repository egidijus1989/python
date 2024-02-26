#funkcionalumas
from tkinter import *

#----------------------------Funkcija kvadratas----------------------------------
def kvadratas():
    tekstas = entry1.get()
    if tekstas != "" and tekstas.isdigit():
        sk = int(tekstas)
        kvadratu = sk * sk
        atsakymotekstas = f'skaicio {sk} kvadratas yra {kvadratu}'
        label2.configure(text=atsakymotekstas)
#--------------------------------------------------------------------------------

window = Tk()
window.title("Pirmas kartas")
window.geometry("500x500")
# window.iconbitmap('pav.ico')

#duomenu etikete
label1 = Label(window, text="parasykite skaiciu...")
label1.place(x=10, y=10)

#ivesties laukas
entry1 = Entry(window)
entry1.place(x=10, y=30)

#mygtukai kuriam
button1 = Button(window, text='pakelk kvadratu', command=kvadratas)
button1.place(x=150, y=25)

#rezultato ibedimas
label2 = Label(window)
label2.place(x=10, y=60)

window.mainloop()