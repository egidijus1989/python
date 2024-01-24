#ivedus 5 programa apskaiciuoja faktoriala forma 5! = 1 * 2 * 3 * 4 * 5 = 120

n = int(input('Iveskite skaiciu '))
sk = 1
print(f'{n}! = ', end='')
for i in range(1, n+1):
    sk = sk * i
    if i != n:
        print(f'{i}', end=' * ')
    else:
        print(f'{i}', end=' = ')
print(f'{sk}')