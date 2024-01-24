#atspausdinti visus penkiazenklius skaicius, kuriu skaitmenu suma lygi skaitmenu sandaugai
#suskaiciuoti kiek ju yra
kiek = 0
for i in range(10000, 99999):
    x1 = i // 10000
    x2 = i // 1000 % 10
    x3 = i // 100 % 10
    x4 = i // 10 % 10
    x5 = i % 10
    sd = x1 *x2 *x3 *x4 *x5
    sum = x1 +x2 +x3 +x4 +x5
    if (sum == sd):
        print(i, end=(", "))
        kiek += 1
print(f'ju yra {kiek}')