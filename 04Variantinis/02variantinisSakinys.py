

diena = int(input('iveskite dienos skaiciu '))

viskasOK = True
match diena:
    case 1 | 2 | 3| 4 | 5 :
        txt = 'darbo diena'
    case 6 | 7 :
        txt = 'savaitgalis'
    case _:
        print('blogai ivesti duomenys')
        viskasOK = False
 
if viskasOK :       
    print(f'{diena} - {txt}')