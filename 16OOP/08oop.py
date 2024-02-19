import time

#funkcija
def kiekLaiko(func):
    def pradziaPabaiga(*args, **kwargs):
        pradzia =time.time()
        rez = func(*args, **kwargs)
        pabaiga =time.time()
        print(f'Funkcijos "{func.__name__}" vykdymo laikas: {pabaiga - pradzia} sek')
        return rez
    return pradziaPabaiga

#primityvi musu funkcija
@kiekLaiko
def musuFunkcija(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma

print(musuFunkcija(10000000))