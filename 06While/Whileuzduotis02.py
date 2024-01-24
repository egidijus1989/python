n = int(input('iveskite skaiciu...'))
first = 0

while n > 0:
    x1 = n % 10
    n //= 10
    print('*' * x1)