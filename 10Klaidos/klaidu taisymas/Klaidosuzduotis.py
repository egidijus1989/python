duomKlaida = []
duomInfo = []

for byla in '\\klaidu taisymas':
    f = open(byla, 'r', encoding='utf-8')
    duomInfo.append(f.read())
    
print(duomInfo)