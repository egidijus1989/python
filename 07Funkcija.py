sar = [8, 7, 9, 4, 1, 12, 3, 5, 8, 7]
#reikia saraso tik su lyginiais

def arLyginis(sk):
    return sk % 2 == 0

lyginiai = list(filter(arLyginis, sar))
print(lyginiai)

nelyginiai =list(filter(lambda n: n % 2 != 0, sar))
print(nelyginiai)