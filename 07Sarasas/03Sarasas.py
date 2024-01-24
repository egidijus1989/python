m = [5, 8, 9, 7, 9, 4, -1]
print(m[1:3])
a = m
print(a)
print(m)
m[0] = 1000
print(a)
print(m)
b = m[1:4]
print(b)
print(m)
m[2] = 99999
print(b)
print(m)
print(id(a))
print(id(m))
b = m[::]
d= m[1:5:2] # paiems masyvo narius nuo pirmo iki 5 kas antra
print(id(b))

c = m.copy()
print(c)