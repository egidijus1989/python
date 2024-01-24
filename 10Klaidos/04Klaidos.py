duomeSar = ['duom1.txt', 'duom2.txt','duom 3.txt','duom4.txt']
duomKlaida = []
duomInfo = []

for byla in duomeSar:
    try:
        f = open(byla, 'r', encoding='utf-8')
        duomInfo.append(f.read())
    except Exception as ex:
        duomKlaida.append(byla)
        
print(f'klaidingi failai {duomKlaida}')
print(f'duomenys: {duomInfo}')