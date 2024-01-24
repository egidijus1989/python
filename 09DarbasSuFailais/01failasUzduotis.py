import random

def rasom1(txt):
    with open('reg.txt', 'a', encoding='utf-8') as f:
        f.write(txt +'\n')
def rasom2(txt):
    with open('reg.txt', 'a', encoding='utf-8') as f:
        f.write(txt +'. ')


def zaidimas():
    n = int(input('iveskite sveika skaiciu...'))
    rasom1(f'Vartotojas įvedė skaičių {n}')
    sk = random.randint(0, n)
    rasom1(f'Sugeneruotas atsitiktinis skaičius {sk}')
    spejimuSk = 0
    blogiSpejimai = 0

    while True:
        spejimas = int(input('spekite kompiuterio sugeneruota skaiciu...'))
        rasom2(f'x spėjimu vartotojas įvedė {spejimas}')
        if spejimas < 0 or spejimas > n:
            print('negalimas spejimas, pakartokite spejima')
            blogiSpejimai += 1

        spejimuSk += 1
        if spejimas == sk:
            print('jus atspejote')
            print(f'kompiuterio sugeneruotas skaicius buvo {sk}')
            print(f'is viso spejote {spejimuSk - blogiSpejimai} tinkamus kartus, bandymu ivesti netinkama skaiciu buvo {blogiSpejimai}')
            rasom1(f'\n{spejimuSk} spėjimu vartotojas atspėjo skaičių')
            m = input('ar norite dar karta zaisti(T/N) ')
            if m != 'T':
                rasom1(f'Į užklausą „Ar žaisite dar“ pasirinko „Ne“')
                break
            else:
                rasom1(f'Į užklausą „Ar žaisite dar“ pasirinko „Taip“')
                zaidimas()
        elif spejimas > sk:
            print(f'kompiuterio sugeneruotas skaicius yra mazesnis nei jusu spetas {spejimas}')
            rasom1(f'Atsakymas – sugeneruotas skaičius mažesnis')
        elif spejimas < sk:
            print(f'kompiuterio sugeneruotas skaicius yra didesnis nei jusu spetas {spejimas}')
            rasom1(f'Atsakymas – sugeneruotas skaičius didesnis')
        

zaidimas()