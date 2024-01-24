sar1 = [2, 4, -5, 6, -8, 4, 7, 5]
sar2 = [-1, -2, 4, 3, 2.5, -2, 5]
sarNul =[]
for x in sar1:
    for y in sar2:
        sumaNul = x + y * 2
        if sumaNul == 0:
            sarNul.append([x, y])
print(sarNul)

sar0 = [[x, y] for x in sar1 for y in sar2 if x+2*y==0]
print(sar0)