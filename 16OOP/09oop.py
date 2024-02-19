#@classmethod
class Robotas:
    def __init__(self, name, age, enable, wheels, force):
        self.name = name
        self.age = age
        self.enable = enable
        self.wheels = wheels
        self.force = force

    @classmethod
    def sukarpyti(cls, eilute):
        name, age, enable, wheels, force = eilute.split(", ")
        age = int(age)
        wheels = int(wheels)
        enable = bool(enable)
        return cls(name, age, enable, wheels, force)

dulkiuSiurblys = Robotas.sukarpyti('Xiomi, 2, True, 3, 0.47KW')

print(dulkiuSiurblys.__dict__)