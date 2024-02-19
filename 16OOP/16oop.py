#__getattr_
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __getattr_(self, item):
        print(f'Norime kreiptis i neegzistiojanti atributa {item}')
        return None


pt1 = Point(10, 20)
pt2 = Point(1, 2)


# print(pt1.z)
print(pt1.x)