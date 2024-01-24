#apskaiciuoti prekiu pvm
def pvm1 (x1, x2, x3):
    return sum([x1, x2, x3]) * 0.21

def pvm2(*args):
    print(type(args))
    return sum(args) * 0.21

pvmDydis1 = pvm1(15.25, 18.36, 20.54)
print(pvmDydis1)

pvmDydis3 = pvm2(15.25, 18.36, 20.54, 25.47)
print(pvmDydis3)

pvmDydis4 = pvm2(15.25, 18.36)
print(pvmDydis4)