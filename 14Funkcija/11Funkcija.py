#map(funkcija, iteruojamas dydis)

def kvadratas(sk):
    return sk * sk

sar = [5, 8, 9, 7, 4, -1, 5]
sar2 = [7, 9, 10, 3, 8, -2, 3]
sarKv = list(map(kvadratas, sar))
print(sarKv)

#reikia rasti x - y, kai x > y ir x+y kai x < y

print(list(map(lambda x, y: x -y if x > y else x + y, sar, sar2)))