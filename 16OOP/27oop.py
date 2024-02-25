#kaip paveldejimas veikia __ protected ir _private

class Koordinates:
    name = "Koordinates"
    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

class Staciakampis(Koordinates):
    def __init__(self, x1, y1, x2, y2, uzpildas = None):
        super().__init__(x1, y1, x2, y2)
        self.__uzpildas = uzpildas

    def getKoordinates(self):
        return (self._x1, self._y1, self._x2, self._y2,)

st1 = Staciakampis(1, 1, 10, 20, "Red")
print(st1.__dict__)
print(st1.getKoordinates())