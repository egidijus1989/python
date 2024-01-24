kort = (5, 8, 9, 7 , 9, 4)

kort1 = 5, 8, 9, 7 , 9, 4
print(type(kort1))

kort2 =(2,)
print(type(kort2))

list = [5, 8, 9, 7]
kort4 = tuple(list)

for i in kort1:
    print(i)
    
print(kort1.count(9))
print(kort1.index(5))

k = (5, 8, 9)
k += (5, 9)
print(id(k))
print(k)
print(len(k))