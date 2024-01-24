#ivedami du skaiciai, parasyti programa su funkcijomis, siu skaiciu sumai apskaiciuoti
#modifikuoti taip 12 + 15 = 27
def ivedimas(txt):
    sk = int(input(f'{txt} = '))
    return sk

def sumavimas():
    sk1 = ivedimas('Pirmas')
    sk2 = ivedimas('Antras')
    suma = sk1 + sk2
    return suma, sk1, sk2

def rezultatas():
    #print(sumavimas)
    rez, a, b = sumavimas()
    print(f'{a} + {b} = {rez}')
    
rezultatas()