from tkinter import *

window = Tk()
window.title("Pirmas kartas")
window.geometry("500x500")
window.iconbitmap("pav.ico")

#galimi elementai
#etikete--------------------------------------------------------------------------------------
label1 = Label(window, text="Etikete")
label1.grid(row=0, column=0)
#mygtukas------------------------------------------------------------------------------------
button1 = Button(window, text="mygtukas")
button1.grid(row=1, column=1)
#ivesties laukas------------------------------------------------------------------------------
entry1 = Entry(window, text="ivesties laukas")
entry1.grid(row=2, column=2)
#dropdwnas selektas--------------------------------------------------------------------------
sarasas = ["Knyga", "Plansete", "Mobyliakas", "Kompiuteris"]
var = StringVar(value=sarasas)
listbox1 = Listbox(window, listvariable=var)
listbox1.grid(row=3, column=3)
#zymejimo laukas----------------------------------------------------------------------------
var1 = IntVar
checkas1 = Checkbutton(window, text="kazkas", variable=var1, onvalue=1, offvalue=0, command="")
checkas1.grid(row=4, column=4)
#pasirinkimas---------------------------------------------------------------------------------
var2 = IntVar()
r1 = Radiobutton(window, text="pasirinkimas", variable=var2, value=1, command="")
r2 = Radiobutton(window, text="pasirinkimas", variable=var2, value=2, command="")
r1.grid(row=5, column=0)
r2.grid(row=6, column=0)
#skale-----------------------------------------------------------------------------------------
var3 = IntVar()
s1 = Scale(window, variable=var3, from_=-1, to=100, orient=HORIZONTAL)
s1.grid(row=7, column=1)
#drobe-----------------------------------------------------------------------------------------
drobe= Canvas(window, bg="white", height=200, width=200)
drobe.grid(row=8, column=2)
img = PhotoImage(file="pitonas.png")
paveikslelis=drobe.create_image(0, 0, image = img)
drobe.create_line(50, 150, 150, 150, fill="red", width=5)
drobe.create_rectangle(150, 50, 200, 100, fill="green", outline="blue")
#teksto laukas--------------------------------------------------------------------------------
t = Text(height=5, width=20, yscrollcommand=SCROLL, wrap="char")
t.insert(END,"Cia mano tekstas")
t.config(font=("Comic Sans Ms", 16, "bold"))
t.grid(row=9, column=0)

window.mainloop()
