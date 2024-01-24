pinigu_suma = input("Iveskite pinigu suma, eurus nuo centu atskirkite tasku...")
x = pinigu_suma.split(".")
eurai = x[0]
centai = x[1]

if x[-1] == 1:
    centu_zodis = "centas"
else:
    centu_zodis = "centai"
print(centu_zodis)