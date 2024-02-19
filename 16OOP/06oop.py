class Robotas:
    def __init__(self, name=None, age=None, enable=None, wheels=None, force=None):
        self.set_data(name, age, enable, wheels, force)
        self.get_data()

    def set_data(self, name, age, enable, wheels, force):
        self.name = name
        self.age = age
        self.enable = enable
        self.wheels = wheels
        self.force = force

    def get_data(self):
        txt = f"Cia startavo robotas {self.name}.\nJo charakteristika:\nAmzius - {self.age}\nVariklio galia - {self.force}"
        return print(txt)
    
    def __del__(self):
        print("Objektas", self, "Pasalintas")
    


languRobotas = Robotas("Noname", 1, True, 0, "0.25kW")
dulkiuRobotas = Robotas("Xiomi", 3, False, 3, "0.45kW")


virtuvesKombainas = Robotas(name="Kopustas", age=1, force="0.85kW")
virtuvesKombainas.get_data()
print(virtuvesKombainas.__dict__)
virtuvesKombainas = 5 #priskiriant kintamojo pavadinima kitam kintamajam objektas istrinamas
print(virtuvesKombainas)