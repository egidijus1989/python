#paveldejimo savybes
class Robotai:
    def __init__(self, name, age, enable, force):
        self.name = name
        self.age = age
        self.enable = enable
        self.force = force

class DulkiuSiurbliaiRobotai(Robotai):
    def __init__(self, name, age, enable, force, wheel, siurbimoGalia, dulkiuTalposTuris, plovimoFunkcija ):
        super().__init__(name, age, enable, force)
        self.wheel = wheel
        self.siurbimoGalia = siurbimoGalia
        self.dulkiuTalposTuris = dulkiuTalposTuris
        self.plovimoFunkcija = plovimoFunkcija

class LanguPlovimoRobotai(DulkiuSiurbliaiRobotai):
    def __init__(self, name, age, enable, force, wheel, siurbimoGalia, dulkiuTalposTuris, plovimoFunkcija, plovimoPavForma, skyscioPurskimoFunkcija, valdymoPultelis):
        super().__init__(name, age, enable, force, wheel, siurbimoGalia, dulkiuTalposTuris, plovimoFunkcija)
        self.plovimoPavForma = plovimoPavForma
        self.skyscioPurskimoFunkcija = skyscioPurskimoFunkcija
        self.valdymoPultelis = valdymoPultelis

kazkoksRobotas = Robotai(force = 1.1, name = "Alexis", age =  2, enable = True)
kazkoksRobotasSiurblys = DulkiuSiurbliaiRobotai("Xiomi", 1, True, 0.45, 3, 0.25, 0.5, False)
kazkoksRobotasPlovimo = LanguPlovimoRobotai('NoName', 2, False, None, 0.8, None, True, 0.2, 'Staciakampis', True, False)

print(kazkoksRobotas.__dict__)
# print(kazkoksRobotasSiurblys.__dict__)
print(kazkoksRobotasPlovimo.__dict__)