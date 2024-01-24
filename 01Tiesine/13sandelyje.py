#sandeluje yra p prekiu ir dideles ir mazos dezes
#i dideliu deziu telpa d prekiu o i maza m prekiu
#kiek reikes dideliu ir mazu deziu ir kiek netilps prekiu
#pvz p = 259, d = 10, m = 5
# reikes 25 dideliu, 1 maza ir 4 netilps
p = int(input('Iveskite prekiu skaiciu'))
d = int(input('Iveskite dideliu deziu dydi'))
m = int(input('Iveskite mazu deziu dydi'))
dd = p // d
mm = (p - dd * d) // m
l = p - dd * d - mm * m
print(f'Reikes {dd} dideliu deziu, {mm} mazu deziu ir liks {l} nesupakuotu prekiu')