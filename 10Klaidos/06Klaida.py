import math

def trikampioPlotas(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Krastine turi buti didesne uz 0')
    p = (a + b + c) /2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
    
tr1 = trikampioPlotas(-2, 10, 10)

print(tr1)