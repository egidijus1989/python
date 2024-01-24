#petriuko pazymiai ir vidurkis
n = int(input('kiek petriukas turi pazymiu '))
suma = 0
for i in range(1, n+1):
    paz = int(input(f'Iveskite {i} pazymiu'))
    if 1 <= paz <=10:
        suma = suma + paz
    else:
        print('Blogas pazymys, kartokite ivedima')
        i = i - 1
vid = suma / n
print(f'petriuko pazymiu vidurkis yra {vid}')
#reikia arba su while daryti ar funkcija su rekursija