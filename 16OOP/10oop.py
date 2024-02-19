#@classmethod
# @staticmethod
class Robotas:
    VAL_PER_METUS = 200
    def __init__(self, name, force):
        self.name = name
        self.force = force
        # self.info(name, force)
        self.info()

    @staticmethod
    def enegrijosVienetas():
        return "kWh"

    @staticmethod
    def sunaudojamaMetams(galia):
        return Robotas.VAL_PER_METUS * galia

    @classmethod
    def sukarpyti(cls, eilute):
        name, force = eilute.split(", ")
        force = float(force)
        return cls(name, force)
    
    # def info(self, name, force):
    #     print(f'{name} variklio galia {force} kw. Per metus sunaudos {self.sunaudojamaMetams(force)} {self.enegrijosVienetas()}')

    def info(self):
        print(f'{self.name} variklio galia {self.force} kw. Per metus sunaudos {Robotas.sunaudojamaMetams(self.force)} {Robotas.enegrijosVienetas()}')

dulkiuSiurblys = Robotas.sukarpyti('Xiomi, 0.47')

# print(dulkiuSiurblys.__dict__)