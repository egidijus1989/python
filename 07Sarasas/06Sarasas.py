#petriuko pazymiai, suvedame, atspausdiname, apskaiciuojame vidurki, mamai rodome didesnius uz 3, teciui didesnius uz 5
# gavome uzsakome visai klasei
MAMA = 4
TATA = 6
#-----------------------Kiek pazymiu funkcija-------------------------------------
def kiekis(vardas):
    kiek = int(input(f'kiek {vardas} turi pazymiu...'))
    return kiek
#---------------------------------------------------------------------------------
#-----------------------Pazymius grazinanti funkcija------------------------------
def gautiPazymius(kiek, vardas):
    paz =[]
    i = 0
    while i < kiek:
        p = int(input(f'Iveskite {vardas} {i +1} pazimi...'))
        if 1<=p<=10:
            paz.append(p)
            i += 1
        else:
            print('Blogas ivedimas. Kartokite ivedima')
    return paz
#---------------------------------------------------------------------------------
#----------------------Vidurkis---------------------------------------------------
def vidurkis(paz):
    if len(paz) == 0:
        return 0
    else:
        vid = sum(paz) / len(paz)
        return vid
#---------------------------------------------------------------------------------
#-------------------------Pazymiai tevams-----------------------------------------
def tevams(paz, kriterijus):
    tevPaz = []
    for i in paz:
        if i >= kriterijus:
            tevPaz.append(i)
    return tevPaz
#---------------------------------------------------------------------------------
#--------------------------Rezultato funkcija-------------------------------------
def rezultatas(vardas):
    paz = gautiPazymius(kiekis(vardas), vardas)
    pazM = tevams(paz, MAMA)
    pazT = tevams(paz, TATA)
    print(f'{vardas} pazymiai yra {paz}, vidurkis {vidurkis(paz)}')
    print(f'{vardas} mamai pazymiai yra {pazM}, vidurkis {vidurkis(pazM)}')
    print(f'{vardas} tatai pazymiai yra {pazT}, vidurkis {vidurkis(pazT)}')
#---------------------------------------------------------------------------------
klase =['Petras', 'Antanas', 'Jonas', 'Stasys', 'Maryte']
for i in klase:
    rezultatas(i)