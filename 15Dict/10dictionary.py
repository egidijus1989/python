def skaityti():
    with open('./15Dict/data10.txt', 'r', encoding="utf-8") as f:
        eilutes = f.readlines()
        duomenys = {}
        for eilute in eilutes:
            vardas = eilute[:20].strip()
            likusiDalis = eilute[20:].strip()
            duomenys[vardas] = [int(i) for i in likusiDalis.split()]
        return duomenys

def resultatas():
    duomenys = skaityti()
    for k, v in duomenys.items():
        duomenys[k].append(3*v[0] + 2*v[1] + v[3])
    return duomenys

def spausdinti(komanda):
    with open("./15Dict/rez10.txt", "a", encoding="utf-8") as f:
        f.write("\n-------------------------------------------------------------\n")
        f.write("| Vardas            | Viso: | 3 t. | 2 t. | 1 t. | Pr |\n")
        f.write("\n-------------------------------------------------------------\n")
        for vardas, taskai in komanda.items():
            f.write(f'| {vardas:18} | {taskai[4]:4} | {taskai[0]:4} | {taskai[1]:4} | {taskai[2]:4} | {taskai[3]:4} |\n')
        f.write("\n-------------------------------------------------------------\n")

def valyti():
    with open("./15Dict/rez10.txt", "w") as f:
        pass

valyti()
komanda = resultatas()
spausdinti(komanda)
komandaSurikiuotaRez = dict(sorted(komanda.items(), key = lambda kv:-kv[1][4] ))
spausdinti(komandaSurikiuotaRez)
komandaSurikiuotaRezViskas = dict(sorted(komanda.items(), key = lambda kv:(-kv[1][4], -kv[1][0], -kv[1][1], -kv[1][2], kv[1][3]) ))
spausdinti(komandaSurikiuotaRezViskas)



