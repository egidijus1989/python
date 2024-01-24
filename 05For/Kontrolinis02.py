sum = 0
for i in range (1000, 9999):
    x1 = i // 100
    x2 = i - x1 *100
    if (x1 + x2) * (x1 + x2) == i:
        sum = sum + 1
        print(i)
print(sum)