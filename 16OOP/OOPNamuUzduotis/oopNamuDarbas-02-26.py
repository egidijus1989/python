class Zaidejas:
    komandosTaskai = 0
    def __init__(self, vardas, ugis):
        pass
        self.vardas = vardas
        self.ugis = ugis
        self.pataikytiTritaskiai = 0
        self.pataikytiDvitaskiai = 0
        self.pataikytosBaudos = 0
        self.prazanguKiekis = 0

    def zaidejoTaskaiViso(self, pataikytiTritaskiai, pataikytiDvitaskiai, pataikytosBaudos):
        print(f'Zaidejas is viso imete {pataikytiTritaskiai * 3 + pataikytiDvitaskiai * 2 + pataikytosBaudos} tasku')
        Zaidejas.komandosTaskai += (pataikytiTritaskiai * 3 + pataikytiDvitaskiai * 2 + pataikytosBaudos)

    def baigeRungtynes(self, prazanguKiekis):
        if prazanguKiekis == 5:
            print(f'Zaidejas baige varzybas del prazangu')
            return True
        else:
            print(f'Zaidejas vis dar gali zaisti')
            return False
    def info(self, pataikytiTritaskiai, pataikytiDvitaskiai, pataikytosBaudos, prazanguKiekis):
        visoTaskai = pataikytiTritaskiai * 3 + pataikytiDvitaskiai * 2 + pataikytosBaudos
        if prazanguKiekis == 5:
            x = "jis nebegali zaisti"
        else:
            x =  "jis vis dar gali zaisti"
        print(f'Zaidejas imete {pataikytiTritaskiai} tritaskius, {pataikytiDvitaskiai} dvitaskius, {pataikytosBaudos} baudas, surinko {visoTaskai}, {x}, jo ugis yra {self.ugis} cm')
    def visoSurinko():
        return Zaidejas.komandosTaskai

zaidejas1 = Zaidejas("Jonas Jonaitis", 195)
zaidejas2 = Zaidejas("Petras Petraitis", 211)
zaidejas3 = Zaidejas("Kazys Kazkauskas", 206)

zaidejas1.zaidejoTaskaiViso(3, 8, 5)
zaidejas1.baigeRungtynes(4)
zaidejas1.info(3, 8, 5, 4)
zaidejas2.zaidejoTaskaiViso(1, 11, 8)
zaidejas2.zaidejoTaskaiViso(2, 5, 1)

komandosBenriTaskai = Zaidejas.visoSurinko()

print(f'Komanda bendrai surinko {komandosBenriTaskai} tasku')