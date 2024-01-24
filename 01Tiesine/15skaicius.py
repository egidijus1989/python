# isivedame sesiazenkli skaiciu 456789
sk = int(input('iveskite sesiazenkli skaiciu'))
x1 = sk // 100000
x2 = sk // 10000 % 10
x3 = sk // 1000 % 10
x4 = sk // 100 % 10
x5 = sk // 10 % 10
x6 = sk %10
suma = x1 +x2 +x3 +x4 + x5 + x6
print(f'skaiciaus{sk} skaitmenu suma = {suma}')