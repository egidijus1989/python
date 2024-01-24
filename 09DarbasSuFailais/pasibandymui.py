def ivedimas(txt):
    sk = int(input(txt +" = "))
    return sk

def rasom1(txt):
    with open('data6.txt', 'a', encoding='utf-8') as f:
        f.write(txt +'\n')
        
kiek = int(input('kiek skaiciu norite sumuoti> '))
rasom1(f'Vartotojas ives {kiek} skaicius')
sum = 0
for i in range(1, kiek+1):
    sk = ivedimas(f'sk{i} ')
    rasom1(f'sk{i} = {sk}')
    sum += sk
rasom1(f'suma = {sum}')