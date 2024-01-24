#**kwargs

def visoTaskai(**kwargs):
    suma = 0
    for k, v in kwargs.items():
        print(f'Zaidejas {k} surinko {v} tasku')
        suma += v
    return suma
komandaA = visoTaskai(Algis = 25, Jonas = 24, Antanas = 13, John = 28, Petras = 17)

print(komandaA)