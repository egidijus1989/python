def skaityti():
    with open('./15Dict/duom12.txt', 'r', encoding="utf-8") as f:
        tekstas = f.read()
        # tekstas = tekstas.replace(" ", '').replace('\n', '')
        tekstas = tekstas.lower()
        simboliai = set(tekstas)
        dictSimboliai = dict.fromkeys(list(simboliai), 0)
        for raide in dictSimboliai.keys():
            dictSimboliai[raide] = tekstas.count(raide)
        return dictSimboliai
    
def spausdinti(rezultatas):
    with open("./15Dict/rez12.txt", "a", encoding="utf-8") as f:
        for raide, kiekis in rezultatas.items():
            f.write(f' Simboliu {raide} yra {kiekis}\n')
        f.write("\n-------------------------------------------------------------\n")


duomenys = skaityti()
duomenys = dict(sorted(duomenys.items(), key = lambda kv: -kv[1]))
spausdinti(duomenys)