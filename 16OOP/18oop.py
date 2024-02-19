#__delattr_
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __delattr__(self, item):
        if item in('x', 'y'):
            print(f'trinti negalime atributo "{item}"')
        else:
            # object.__delattr__(self, item)
            del self.__dict__[item]

pt1 = Point(10, 20)
pt2 = Point(1, 2)
pt1.z = 15
print(pt1.__dict__)
del pt1.x
print(pt1.__dict__)
del pt1.z
print(pt1.__dict__)