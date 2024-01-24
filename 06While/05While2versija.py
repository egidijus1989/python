#ivedamas bet koks skaicius, rasti to skaiciaus skaitmenu suma

def sumavimas(skaicius):
    suma = 0
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius //= 10
        suma += x1
    return suma
    
sk = int(input('iveskite skaiciu...'))
sumaKita = sumavimas(sk)
print(f'skaiciaus {sk} skaitmenu suma = {sumaKita}')