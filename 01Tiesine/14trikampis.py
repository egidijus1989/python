#turime statu trikampi, statini a ir izambine c, rasti plota s
# s = (a * b) / 2
import math
a = float(input('a='))
c = float(input('c='))
#b = math.sqrt(math.pow(c,2) - math.pow(a,2))
b = math.sqrt(c**2 - a**2)

s = (a * b) / 2
print(f'Trikampio plotas lygus {s}')