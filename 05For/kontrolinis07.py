n = int(input('kiek saleje yra eiliu...'))
k = int(input('kiek kedziu stovi pirmoje eileje...'))
sum = k

for i in range(1, n):
    k = k + 2
    sum = sum + k
print(f'Reikia užsakyti s = {sum} kedziu')