aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 8, 11}
aibeC = {12, 13, 14, 15}
aibeD = {1, 2, 5, 6}

#ar poaibis? true
print(aibeA.issubset(aibeB))

#ar virsaibis? true
print(aibeB.issuperset(aibeA))

#ar visi skirtingi? true

print(aibeC.isdisjoint(aibeB))

#aibiu sajunga

aibeE = aibeA.union(aibeD)
print(aibeE)

#aibiu sankirta
aibeF = aibeA.intersection(aibeD)
print(aibeF)

#skirtumas
aibeG = aibeA.difference(aibeD)
aibeG1 = aibeA.difference_update(aibeD)
print(aibeG)
print(aibeG1)

aibeG2 = aibeC.symmetric_difference(aibeD)
aibeG3 = aibeC.union(aibeD)
print(aibeG2)
print(aibeG3)