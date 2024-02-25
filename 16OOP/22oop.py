#paveldejimo savybes polimorfizmas magiskas metodas __str__
class Robotai:
    def __init__(self, name, age, enable, force):
        self.name = name
        self.age = age
        self.enable = enable
        self.force = force

    def __str__(self):
        return f'Priklauso klasei {self.__class__.__name__}\nName: {self.name}\nAge: {self.age}\nAr ijungtas? {self.enable}\nVariklio galia: {self.force}\n'

class DulkiuSiurbliaiRobotai(Robotai):
    def __init__(self, name, age, enable, force, wheel, siurbimoGalia, dulkiuTalposTuris, plovimoFunkcija ):
        super().__init__(name, age, enable, force)
        self.wheel = wheel
        self.siurbimoGalia = siurbimoGalia
        self.dulkiuTalposTuris = dulkiuTalposTuris
        self.plovimoFunkcija = plovimoFunkcija
    def __str__(self):
        return super().__str__() + f'Ratu skaicius: {self.wheel}\nSiurbimo galia: {self.siurbimoGalia}\nKonteinerio talpa: {self.dulkiuTalposTuris}\nAr plauna: {self.plovimoFunkcija}\n'

class LanguPlovimoRobotai(Robotai):
    def __init__(self, name, age, enable, force, plovimoPavForma, skyscioPurskimoFunkcija, valdymoPultelis):
        super().__init__(name, age, enable, force)
        self.plovimoPavForma = plovimoPavForma
        self.skyscioPurskimoFunkcija = skyscioPurskimoFunkcija
        self.valdymoPultelis = valdymoPultelis
    def __str__(self):
        return super().__str__() + f'Plovimo pavirsius: {self.plovimoPavForma}\nAr purskia: {self.skyscioPurskimoFunkcija}\nAr yra valdymo pultelis?: {self.valdymoPultelis}\n'

kazkoksRobotas = Robotai("Alexis", 2, True, 1.1)
kazkoksRobotasSiurblys = DulkiuSiurbliaiRobotai("Xiomi", 1, True, 0.45, 3, 0.25, 0.5, False)
kazkoksRobotasPlovimo = LanguPlovimoRobotai('NoName', 2, False, 0.2, 'Staciakampis', True, False)

print(kazkoksRobotas)
print(kazkoksRobotasSiurblys)
print(kazkoksRobotasPlovimo)