txt = '11, 22, 33, 41, 51, 61, 17, 18, 19, 25, 24, 26, 37, 38, 39'
#is txt gauti lyginiu skaiciu sarasa
sk =[int(i) for i in txt.split(', ') if int(i) % 2 == 0]# pirma dalis iskarpo i masyva, antra paima tik lyginius
print(sk)