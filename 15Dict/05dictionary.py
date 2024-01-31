with open('./15Dict/duom1.txt', 'r', encoding='utf-8') as f:
    txtlist = f.readlines()
    
print(txtlist)
komanda = {}
for txt in txtlist:
    mas = txt.split(":")
    taskai = mas[1].replace(",","")
    komanda[mas[0]] = int(taskai)
print(komanda)