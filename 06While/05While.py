#ivedamas bet koks skaicius, rasti to skaiciaus skaitmenu suma

sk = int(input('iveskite skaiciu...'))
kopija = sk
suma = 0
while sk > 0:
    x1 = sk % 10
    sk = sk // 10 #sk //= 10
    suma += x1
print(f'skaiciaus {kopija} skaitmenu suma = {suma}')