aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 8, 11}
aibeC = {12, 13, 14, 15}
aibeD = {1, 2, 5, 6}

#update nesukuria naujos aibes, oniom sukuria nauja aibe
aibeA.update(aibeB)
print(aibeA)

#pasalinti elementus,
#remove salina tik egzituojancius, meta klaida
aibeA.remove(1)
print(aibeA)

#discard nera klaida jei elementas neegzistuoja
aibeA.discard(2)
print(aibeA)

#grazina salinama reiksme
kazkas = aibeA.pop()
print(kazkas)

#istrinti visa aibe
aibeC.clear()
print(aibeC)