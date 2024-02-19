class Robotas:
    name = None
    age = None
    enable = None

    def startuos(self, val, min):
        self.val = val
        self.min = min
    def getStartRobot(self):
        return self.val, self.min

languRobotas = Robotas()
dulkiuRobotas = Robotas()

languRobotas.startuos(9, 45)
dulkiuRobotas.startuos(19, 45)
print(f'Dulkiu siublys stratuoja {dulkiuRobotas.getStartRobot()}')
print(f'Langu robotas stratuoja {languRobotas.getStartRobot()}')