import math
m = int(input('iveskite knygos paskutinio puslapio skaiciu...'))
sum = 0
for i in range(1, m+1):
    digits = int(math.log10(i))+1
    if digits == 3:
        sum = sum + 3
    elif digits == 2:
        sum = sum + 2
    elif digits == 1:
        sum = sum + 1
    
print(f'Knygai sunumeruoti reikia {sum} skaitmenu')