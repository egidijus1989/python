m = int(input('iveskite bilietu imties pradini bilieta...'))
n = int(input('iveskite bilietu imties paskutini bilieta...'))
sum = 0

for i in range(m, n):
    x1 = i // 1000
    x2 = i - x1 * 1000
    if x1 == x2:
        sum = sum + 1
        
print(f'Laimingus bilietus įsigijo {sum} keleiviu')