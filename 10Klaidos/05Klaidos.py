import sys

duomeSar = ['duom1.txt', 'duom2.txt','duom 3.txt','duom4.txt']
duomKlaida = []
duomInfo = []
try:
    for byla in duomeSar:
        try:
            f = open(byla, 'r', encoding='utf-8')
            duomInfo.append(f.read())
        except Exception as ex:
            duomKlaida.append(byla)
            sys.exit()
finally:
    f = open('logo.txt', 'w')
    for i in duomInfo:
        f.write(f'gerai issaugoti duomenys: {i}')
        f.write('\n')
    f.write(str(f'klaidingi duomenys: {duomKlaida}'))
    f.close() 