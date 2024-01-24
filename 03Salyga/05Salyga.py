#ivedami 2 skaiciai, surasti didziausia ir maziausia nenaudojant min ir max
a =int(input('a = '))
b =int(input('b = '))

if a > b:
    did = a
    maz = b
    print(f'{did} didziausias, o {maz} maziausias')
elif a < b:
    did = b
    maz = a
    print(f'{did} didziausias, o {maz} maziausias')
else:
    print('skaiciai lygus')