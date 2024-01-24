#apversti skaiciu

def atvir(skaicius):
    atv = 0
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius //= 10
        atv = atv * 10 + x1
    return atv
    
sk = int(input('iveskite skaiciu...'))
atvirksciai = atvir(sk)
print(f'skaiciaus {sk} atvirktinis skaicius = {atvirksciai}')