class Robotas:
    "Labai svarbus dalykas dokumentacija"
    name = None
    age = None
    enable = None

    def pasisveikinti(self):
        print("Labas. As esu ", self)

# print(Robotas.__doc__)
# print(list.__doc__)
languRobotas = Robotas()
Robotas.pasisveikinti(languRobotas)
languRobotas.pasisveikinti()