prekes = {
    "Duona": 1.25,
    "Vanduo": 0.65,
    "Konservai": 2.45,
    "Vaisvandeniai": 1.59,
    "Mesa": 7.95,
    "Zuvis": 8.25
}

def perkam():
    suma=0
    while True:
        vienaPreke=input(f'Ka perkam? {list(prekes.keys())}: ')
        if vienaPreke=='end':
            break
        elif vienaPreke not in prekes:
            print('Tokios prekes nera')
            continue
        suma+=prekes[vienaPreke]
    return suma
 
print(perkam())