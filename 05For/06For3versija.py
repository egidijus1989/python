#Petriuko pazymiai surasti pirma didziausia ir kelintas jis buvo
def ivedimas(nr):
    paz = int(input(f'Iveskite {nr}-aji pazymi '))
    if 1 <= paz <=10:
        return paz
    else:
        print('Blogas pazymys, kartokite ivedima')
        return ivedimas(nr)
    
n = int(input('kiek petriukas turi pazymiu '))
#did = kelintas = 0
for i in range(1, n+1):
    p = ivedimas(i)
    if i == 1:
        did = p
        kelintas = i
    elif did <= p:
        did = p
        kelintas = i
        
    
print(f'Petriuko didziausias pazimys yra {did}, kuris yra {kelintas} pazymys')