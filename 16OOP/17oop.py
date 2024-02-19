#__delattr_
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __delattr__(self, item):
        print(f'Startavo matodas __delattr__. Bandom trinti "{item}"')
        object.__delattr__(self, item)

pt1 = Point(10, 20)
pt2 = Point(1, 2)
print(pt1.__dict__)
del pt1.x
print(pt1.__dict__)