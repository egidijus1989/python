#kaip paveldejimas veikia __ protected ir _private

class Koordinates:
    name = "Koordinates"
    def __init__(self, x1, y1, x2, y2):
        print(f'Startavo klases Koordinates __init__ {self.__class__}')
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getKoordinates(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2,)

class Staciakampis(Koordinates):
    def __init__(self, x1, y1, x2, y2, uzpildas = None):
        super().__init__(x1, y1, x2, y2)
        print(f'Startavo klases Staciakampis __init__ {self.__class__}')
        self.__uzpildas = uzpildas
    

st1 = Staciakampis(1, 1, 10, 20, "Red")
print(st1.__dict__)
print(st1.getKoordinates())