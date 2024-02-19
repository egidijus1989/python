class Robotas:
    name = None
    age = None
    enable = None

    def startuos(self, val, min):
        self.val = val
        self.min = min

languRobotas = Robotas()
dulkiuRobotas = Robotas()

languRobotas.startuos(9, 45)
dulkiuRobotas.startuos(19, 45)
print(languRobotas.__dict__)
print(f'Langu robotas startuos {languRobotas.val} val. ir {languRobotas.min} min')