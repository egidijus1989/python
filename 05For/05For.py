#atspausdinti visus skaicius nuo 1 iki n, jei patenka 13 ties juo uzbaigti

n = int(input('skaicius = '))
for i in range(1, n):
    if i ==13:
        break
    print(i, end=(', '))
else:
    print('\nCiklas uzbaigtas')
print('Kiti skaiciai....')