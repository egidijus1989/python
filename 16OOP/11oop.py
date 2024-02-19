class Robotas:
    def __init__(self, name, force):
        self._name = name
        self._force = force

    # @property
    # def get_name(self):
    #     return self._name
        
    @property
    def name(self):
        return self._name

dulkiuSiublys = Robotas('Xiomi', 0.45)
print(dulkiuSiublys.__dict__)
print(dulkiuSiublys._name)

# print(dulkiuSiublys.get_name)
print(dulkiuSiublys.name)