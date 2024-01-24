m = [5, 8, 9, 7, 9, 4, -1, 5, -5, 8, 9, 7, 4, 4]

def rastiDidziausia(sarasas):
    did = m[0]
    for i in range(1, len(sarasas)):
        if did < sarasas[i]:
            did = sarasas[i]
    return did

d = rastiDidziausia(m)

print(d)
print(m.count(rastiDidziausia(m)))
print(m.index(rastiDidziausia(m)))

print(m.remove(m[4]))
print(m)
print(m.pop(m[0]))
