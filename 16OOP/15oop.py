#__setattr__
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __setattr__(self, key, value):
        print ('Startavo __setatr__ metodas')
        # object.__setattr__(self, key, value)
        if(key in('_x', '_y')): #__init__ leidzia kurti
            if hasattr(self, key): #tikrina ar nera sukurtos jau sitos savybes
                raise ValueError(f'Nustatyti atributai "{key}" negalimi')
            else:
                object.__setattr__(self, key, value)
        elif key == "z":
            object.__setattr__(self, key, value)
        else:
           raise ValueError(f'Nustatyti atributai "{key}" negalimi') 


pt1 = Point(10, 20)
pt2 = Point(1, 2)

pt1.z = 15
# pt1._x = 18 neleis pakeisti reiksmes

print(pt1.__dict__)