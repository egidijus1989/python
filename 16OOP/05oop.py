class Robotas:
    def __init__(self, name=None, age=None, enable=None, wheels=None, force=None):
        self.name = name
        self.age = age
        self.enable = enable
        self.wheels = wheels
        self.force = force

    def get_data(self):
        txt = f"Cia startavo robotas {self.name}.\nJo charakteristika:\nAmzius - {self.age}\nVariklio galia - {self.force}"
        return print(txt)

languRobotas = Robotas("Noname", 1, True, 0, "0.25kW")
dulkiuRobotas = Robotas("Xiomi", 3, False, 3, "0.45kW")

print(dulkiuRobotas.__dict__)
languRobotas.get_data()

virtuvesKombainas = Robotas(name="Kopustas", age=1, force="0.85kW")
virtuvesKombainas.get_data()