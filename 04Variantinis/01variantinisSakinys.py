#ivedu savaites diena skaiciumi, paraso dienos pavadinima

diena = int(input('iveskite dienos skaiciu '))

viskasOK = True
match diena:
    case 1 :
        txt = 'Pirmadienis'
    case 2 :
        txt = 'Antradienis'
    case 3 :
        txt = 'Treciadienis'
    case 4 :
        txt = 'Ketvirtadienis'
    case 5 :
        txt = 'Penktadienis'
    case 6 :
        txt = 'Sestadienis'
    case 7 :
        txt = 'Sekmadienis'
    case _:
        print('blogai ivesti duomenys')
        viskasOK = False
 
if viskasOK :       
    print(f'{diena} - {txt}')