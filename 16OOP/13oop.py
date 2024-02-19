#deleteris

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
        
    @force.deleter
    def force(self):
        pasitikrinimas = input('Ar tikrai trinsime: (T/N)')
        if pasitikrinimas == "T":
            print('Triname savybe force')
            del self._force
        else:
            print('Nieko neistrineme')
        
dulkiuSiublys = Robotas('Xiomi', 0.45)
print(dulkiuSiublys.force)
del dulkiuSiublys.force
print(dulkiuSiublys.force)