# apskaiciuoti rez = 100 / sk
ciklasVeikia = True
while ciklasVeikia:
    try:
        sk = int(input('Iveskite skaiciu...'))
        rez = 100 / sk
        ciklasVeikia: False
    except ValueError as ex:
        print(f'Blogai ivesti duomenys...Klaida: {ex}')
    except ZeroDivisionError as ex:
        print(f'Dalyba is 0...Klaida: {ex}')
    else:
        print('Panasu kad viskas gerai...')
    finally:
        print('Man dzin ar buvo gerai...')
        
print(f'rez = {rez}')