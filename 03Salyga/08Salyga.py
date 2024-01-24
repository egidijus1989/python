#bingo, nustatyti ar lamingas skaicius
sk = int(input('sk = '))

#laimingas = (sk >= 5 and sk <= 10) or (sk >= 15 and sk <= 20)
laimingas = (5<=sk<=10 or 15<=sk<=20)

if laimingas:
    print('Skaicius laimingas')
else:
    print('Skaicius nelaimingas')