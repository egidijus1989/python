n = int(input('n=...'))

sk = 1
sum = True
while sk <= (n // 2):
    sk += 1
    if n % sk == 0:
        sum = False
        break
      
if sum == 2:
    print('skaicius yra pirminis')
else:
    print('skaicius yra sudetinis')