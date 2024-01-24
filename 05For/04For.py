#atspausdinti visus skaicius nuo 1 iki n, jei patenka 13 jo nespausdint

n = int(input('skaicius = '))
for i in range(1, n):
    if i ==13:
        continue
    print(i, end=(', '))
else:
    print('Ciklas uzbaigtas')
print('Kiti skaiciai....')