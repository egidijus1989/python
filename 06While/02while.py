#ivedamas skaicius 12 atspausdinti jo daliklius ir dalikliu skaiciu
n = int(input('n=...'))

sk = 1
sum = 0
while sk <= n:
    if n % sk == 0:
        print(sk, end=(', '))
        sum += 1
    sk += 1
print(f'daugikliu yra {sum}')