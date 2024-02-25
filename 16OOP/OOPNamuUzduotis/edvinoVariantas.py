class Zaidejas:
    visoTasku = 0

    def __init__(self, vardas, pataikytu_tritaskiu_kiekis, pataikytu_dvitaskiu_kiekis, baudos_metimu_kiekis, prazangu_kiekis, ugis):
        self.vardas = vardas
        self.pataikytu_tritaskiu_kiekis = pataikytu_tritaskiu_kiekis
        self.pataikytu_dvitaskiu_kiekis = pataikytu_dvitaskiu_kiekis
        self.baudos_metimu_kiekis = baudos_metimu_kiekis
        self.prazangu_kiekis = prazangu_kiekis
        self.ugis = ugis

    def skaiciuotiTaskus(self):
        self.zaidejoTaskaiViso = self.pataikytu_tritaskiu_kiekis * 3 + self.pataikytu_dvitaskiu_kiekis * 2 + self.baudos_metimu_kiekis
        Zaidejas.visoTasku += self.zaidejoTaskaiViso
    
    @staticmethod
    def visoSurinko():
        return Zaidejas.visoTasku
    
    def baigeRungtynes(self):
        if self.prazangu_kiekis < 5:
            self.baige = True
        else:
            self.baige = False
    
    def info(self):
        print(f'Vardas: {self.vardas}\n\
Tritaskiu: {self.pataikytu_tritaskiu_kiekis}\n\
Dvitaskiu: {self.pataikytu_dvitaskiu_kiekis}\n\
Baudos metimu: {self.baudos_metimu_kiekis}\n\
Prazangu kiekis: {self.prazangu_kiekis}\n\
Surinko tasku: {self.zaidejoTaskaiViso}\n\
Ugis: {self.ugis}\n\
Ar baige rungtynes: {'taip' if self.baige else 'ne' }\n\
--------------------')


zaidejas1 = Zaidejas('Jonas', 3, 2, 1, 3, 198)
zaidejas1.skaiciuotiTaskus()
zaidejas1.baigeRungtynes()
zaidejas1.info()

zaidejas2 = Zaidejas('Petras', 5, 1, 3, 4, 199)
zaidejas2.skaiciuotiTaskus()
zaidejas2.baigeRungtynes()
zaidejas2.info()

print(f'Zaidejai bendrai surinko {Zaidejas.visoSurinko()} tasku')