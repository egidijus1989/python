# __getattribute__

from typing import Any


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __getattribute__(self, item):
        print('metodas __getattribute startavo')
        return object.__getattribute__(self, item)
        # if item == "x":
        #     raise ValueError('Kreptis i x atributa negalima')
        # else:
        #     return object.__getattribute__(self, item)

    @property
    def x(self):
        print('Kreipiames i x')
        # raise ValueError('Kreptis i x atributa negalima')
    
    @property
    def y(self):
        return self._y

pt1 = Point(10, 20)
pt2 = Point(1, 2)

a = pt1.y
print(a)
# b = pt1.x
# print(b)