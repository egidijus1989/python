m = [5, 8, 9, 7, 9, 4, -1]
print(m)
print(type(m))

user = ['Jonas', 18, 1.78, True, [8, 9, 10, 5, 7]]

print(user[0])
print(user[4])
print(user[4][1])

suma = 0
kiek = 0

for i in m:
    suma += i
    kiek += 1
    
print(suma)
print(kiek)
kiekis = len(m)
print(kiekis)

for i in range(len(m)):
    print(f'm[{i}] = {m[i]}')

for i in m:
    print(i)