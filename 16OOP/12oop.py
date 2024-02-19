class Robotas:
    def __init__(self, name, force):
        self._name = name
        self._force = force

    @property
    def force(self):
        return self._force
    
    @force.setter
    def force(self, reiksme):
        if type(reiksme) in (int, float):
            self._force = reiksme
        else:
            raise ValueError('Galia turi buti skaicius')

dulkiuSiublys = Robotas('Xiomi', '0.45')
print(dulkiuSiublys.__dict__)
dulkiuSiublys.force  = 5.8
print(dulkiuSiublys.force)
print(dulkiuSiublys._force)
dulkiuSiublys._force = 1.5
print(dulkiuSiublys.force)
