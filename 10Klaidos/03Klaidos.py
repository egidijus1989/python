# apskaiciuoti rez = 100 / sk
ciklasVeikia = True
while ciklasVeikia:
    try:
        sk = int(input('Iveskite skaiciu...'))
        rez = 100 / sk
        ciklasVeikia: False
    except Exception as ex:
        print(f'Kazkas blogai...{ex}')
    else:
        print('Panasu kad viskas gerai...')
    finally:
        print('Man dzin ar buvo gerai...')
        
print(f'rez = {rez}')