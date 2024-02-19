class Robotas:
    name = None
    age = None
    enbale = None

dulkiuSiurblys = Robotas()
print(type(dulkiuSiurblys))

dulkiuSiurblys.name = "Xiomi"
dulkiuSiurblys.age = 3
dulkiuSiurblys.enbale = False

print(dulkiuSiurblys)

languRobotas = Robotas()
languRobotas.name = "NoName"
languRobotas.age = 1
languRobotas.enbale = True

print(languRobotas.name)
print(dulkiuSiurblys.__dict__)
print(Robotas.__dict__)

print(type(languRobotas) == Robotas)
print(isinstance(languRobotas, Robotas))

dulkiuSiurblys.color = "Black"
print(languRobotas.__dict__)
print(dulkiuSiurblys.__dict__)

setattr(Robotas, "wheels", 3)
print(Robotas.__dict__)
virtuvesKombainas = Robotas()
print(virtuvesKombainas.__dict__)

# print(languRobotas.color) klaida nes neturi splavos
print(dulkiuSiurblys.color)
ats = "deja nera..."
print(getattr(languRobotas, "color", ats))
print(getattr(dulkiuSiurblys, "color", ats))

del Robotas.wheels
print(Robotas.__dict__)

# delattr(Robotas, "circle") trinti galima tik egzistuojancius atributus