#__delattr_
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __delattr__(self, item):
        if hasattr(self, item):
            print(f'trinamas atributas "{item}"')
            del self.__dict__[item]
        else:
            print(f'atributas {item} neegzistuoja')
            

pt1 = Point(10, 20)
pt2 = Point(1, 2)
pt1.z = 15
print(pt1.__dict__)
del pt1.x
print(pt1.__dict__)
del pt1.z
print(pt1.__dict__)
del pt1.o