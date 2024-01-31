#args
sar1 = [4, 8, 9, 7, 9]
sar2 = [5, 8, 9, -1, 25, 8, 7, 9]

#susumuoti lyginiu elementus

def lyginiuSuma(*args):
    sum = 0
    for i in args:
        if i % 2 == 0:
            sum += 1
    return sum

# print(lyginiuSuma(sar1, sar2)) #klaida
# print(lyginiuSuma(5, 8 7, 7, 9, 8, +4, 7, -5, 2, 12))
print(lyginiuSuma(*sar1, *sar2))