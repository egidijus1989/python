txt = 'Man č ė įęčėšėįųųėįęė labai patinka rytais anksti keltis ir eiti i mokykla'
lt = ('ąčęėįšųūĄČĘĖĮŠŲŪ')
kiek = 0
for i in txt:
    print(i)
    if i in lt:
        kiek += 1
        
print(f'Sakinyje "{txt}" yra {kiek} LT simboliu')