def skaityti():
    with open('./15Dict/data11.txt', 'r', encoding="utf-8") as f:
        eilutes = f.readlines()
        duomenys = {}
        for eilute in eilutes:
            kirptiPerKab = eilute.split(', ')
            vardas = kirptiPerKab[0]
            pazTxt = kirptiPerKab[1].split(' ')
            pazymiai = [int(paz) for paz in pazTxt]
            duomenys[vardas] = pazymiai

        return duomenys

def spausdinti(klase):
    with open("./15Dict/rez11.txt", "a", encoding="utf-8") as f:
        for vardas, pazymiai in klase.items():
            f.write(f' {vardas:18} {str(pazymiai)[1:-1]}\n')
        f.write("\n-------------------------------------------------------------\n")

def valyti():
    with open("./15Dict/rez11.txt", "w") as f:
        pass
            
valyti()
klase = skaityti()
spausdinti(klase)
geriausi = dict(sorted(klase.items(), key = lambda kv: -sum(kv[1]) / len(kv[1])))
spausdinti(geriausi)