cars = ["Opel", "Subaru", "Mercedes", "Volvo", "Suzuki", "BMW", "Audi"]
print(max(cars))

disZodis = max(cars, key = lambda car: len(car))
print(disZodis)