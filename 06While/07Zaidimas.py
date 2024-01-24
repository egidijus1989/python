#(A -akmuo, Z - zirkles, P - popierius)
#zaidejas ir kompiuteris

import random
pasirinkimas = input('pasirinkite: A -akmuo, Z - zirkles, P - popierius.....')
zaidimas = random.choice(['A', 'Z', 'P'])
print(f'Jus pasrinkote {pasirinkimas}, kompiuteris pasirinki {zaidimas}')
if pasirinkimas == zaidimas:
    print('lygiosios')
elif pasirinkimas == 'A' and zaidimas == 'Z' or pasirinkimas == 'Z' and zaidimas == 'P' or pasirinkimas == 'P' and zaidimas == 'A':
    print('laimejo jus')
else:
    print('laimejo kompiuteris')