prekes = {
    "Duona": 1.25,
    "Vanduo": 0.65,
    "Konservai": 2.45,
    "Vaisvandeniai": 1.59,
    "Mesa": 7.95
}

print(type(prekes))
print(prekes)

draugai = dict(Tomas = 28, Tadas = 32, Jonas = 51, Stasys = 45)
print(type(draugai))
print(draugai)

priesai = dict.fromkeys(["Vytautas", "Kestas", "Juozas"], [])
print(type(priesai))
print(priesai)

kainaMesa = prekes['Mesa']
print(kainaMesa)
# print(prekes.Mesa) nepavyks
# print(prekes['Vitaminai']) neveiks
print(prekes.get('Vitaminai'))
print(prekes.get('Vitaminai', 'Deja sios prekes neturime'))
print(prekes.get('Duona', 'Deja sios prekes neturime'))
prekes['Pienas'] = 1.65
print(prekes)

del prekes['Vanduo']
print(prekes)

prekiuSar = prekes.keys()
print(type(prekiuSar))
print(prekiuSar)
prekiuSar = list(prekes.keys())
print(prekiuSar)

sutvarkytas = sorted(prekes.keys())
print(sutvarkytas)

# ar yra preke?
print(('Zuvis') in prekes)
print(('Duona') in prekes)

kainos = prekes.values()
print(kainos)
kainos = list(prekes.values())
print(kainos)

for k, v in prekes.items():
    print(f'preke {k} kainuoja {v}')
    
sarasoKopija = prekes.copy()
print(sarasoKopija)

kazkas = prekes.items()
print(kazkas)

prekes.pop('Mesa')
print(prekes)

print(len(prekes))
print(prekes.popitem())
print(prekes)

prekes.setdefault('Pica')
print(prekes)
