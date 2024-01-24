# ivedamas skaicius, apskaiciuojamas kvadratas, jei skaicius
sk = int(input('sk = '))
kv = sk ** 2

laimingas = sk ==13
if laimingas:
    print('laimingas skaicius')
    
print(f'kv = {kv}')
print(laimingas)