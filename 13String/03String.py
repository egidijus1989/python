import time

txt = "mano batai buvo du, bet kazkas atsitiko - nerandu. labai..."
#surasti visas a raides vietas

index_a = []

for simbolisNr in range(len(txt)):
    if txt[simbolisNr] == "a":
        index_a.append(simbolisNr)
print(index_a)

x = "a"
metodas = [pos for pos, char in enumerate(txt) if char == x]
print(metodas)

aNr = []
eil = 0
kiek_a = txt.count("a")
while len(aNr)<kiek_a:
    eil = txt.find("a", eil)
    aNr.append(eil)
    eil += 1