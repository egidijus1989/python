#nelyginius elementus padidinti 1
m = [5, 8, 9, 7, 9, 4, -1]

for i in range(len(m)):
    if m[i] % 2 != 0:
        m[i] = m[i] + 1
    
# for i in m:
#    if i % 2 == 0:
#        i = i + 1
        
print(m)
print(m[len(m)-1])


################################################
a = [5, 55, 555]
naujas = a + m
print(naujas)

m += [6, 66, 666]
print(m)

c = m * 2
print(c)

print(sum(m))

eil = ('54 254 14 25 15 -85')
skaiciai = list(eil.split(' '))
print(skaiciai)

intSkaiciai = [int(i) for i in eil.split(' ')]
print(intSkaiciai)