#@classmethod
class Robotai:
    def __init__(self, name, age, enable, force):
        self.name = name
        self.age = age
        self.enable = enable
        self.force = force

class DulkiuSiurbliaiRobotai:
    def __init__(self, wheel, siurbimoGalia, dulkiuTalposTuris, plovimoFunkcija ):
        self.wheel = wheel
        self.siurbimoGalia = siurbimoGalia
        self.dulkiuTalposTuris = dulkiuTalposTuris
        self.plovimoFunkcija = plovimoFunkcija

class LanguPlovimoRobotai:
    def __init__(self, plovimoPavForma, skyscioPurskimoFunkcija, valdymoPultelis):
        self.plovimoPavForma = plovimoPavForma
        self.skyscioPurskimoFunkcija = skyscioPurskimoFunkcija
        self.valdymoPultelis = valdymoPultelis

kazkoksRobotas = Robotai("Alexis", 2, True, 1.1)
kazkoksRobotasSiurblys = DulkiuSiurbliaiRobotai(3, 0.25, 0.5, False)
kazkoksRobotasPlovimo = LanguPlovimoRobotai('Staciakampis', True, False)

print(kazkoksRobotas.__dict__)
print(kazkoksRobotasSiurblys.__dict__)
print(kazkoksRobotasPlovimo.__dict__)