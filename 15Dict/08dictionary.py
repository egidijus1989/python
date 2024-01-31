def skaitomFaila():
    with open('./15Dict/duom8.txt', 'r', encoding='utf-8') as f:
        txtList = f.readlines()
    return txtList

#raktas ir sarasas - dict forma

def varzybos():
    dalyviai = dict()
    duomenys = skaitomFaila()
    for eil in duomenys:
        vardas, taskai = eil.split()[:2]
        # print(f'{vardas} surinko {taskai}')
        taskai = int(taskai)
        if vardas in dalyviai:
            dalyviai[vardas].append(taskai)
        else:
            dalyviai[vardas] = [taskai]
    return dalyviai

# print(varzybos())

def spausdinti(rez):
    with open("./15Dict/rez8.txt", "a", encoding='utf-8') as f:
        f.write('\n---------------------------------\n')
        f.write("| Vardas   |   Suma    |    Max   |\n")
        f.write('\n---------------------------------\n')
        for vardas, suma, did in rez:
            f.write(f'{vardas: 8} | {suma: 3} | {did: 3} |\n')
        f.write('\n---------------------------------\n')
            
def valyti():
    with open("./15Dict/rez8.txt", "a", encoding='utf-8') as f:
        f.write("")
        

valyti()
dalyviai1 = varzybos()
rezultatai = [(v, sum(t), max(t)) for v, t in dalyviai1.items()]
# print(rezultatai)
spausdinti(sorted(rezultatai))
spausdinti(sorted(rezultatai, key = lambda e: e[1], reverse=True))
spausdinti(sorted(rezultatai, key = lambda e: e[1], reverse=True))

varzybos()