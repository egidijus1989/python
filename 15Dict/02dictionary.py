auto_geras = {
    "Marke" : "Opel",
    "Kaina" : 2500,
    "Turis": 1.4,
    "Dauztas": False 
}
auto_blogas = {
    "Dauztas": False,
    "Kaina" : 2500,
    "Turis": 1.4,
    "Marke" : "Opel",
}

print(auto_geras == auto_blogas)

daugiau_info = {
    "Raida": 245678,
    "Spalva": "Kibiro",
    "Kaina": 3500
}

auto_geras.update(daugiau_info)
print(auto_geras)

kitas_auto = auto_blogas|daugiau_info
print(kitas_auto)
print(auto_geras.keys())
print(auto_blogas.values())
print(auto_geras.items())