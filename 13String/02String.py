txt = "mano batai buvo du, bet kazkas atsitiko - neradu"

print(len(txt))
print(txt[len(txt) -1])
print(txt[-1])

#kiek zodziu
kiekZodziu = txt.count(' ')
print(kiekZodziu)

print(txt.capitalize()) #sakinio stilius

print(txt.upper())
print(txt.lower())
print(txt.islower())
print(txt.isupper())

print(txt.find('a'))
print(txt.find('a', 5, 15))
print(txt.find('ch', 5, 15))

t = '123 abc 456 '
t1 ='rvcecrevtrh'
t5 = ' '
print(t.isalnum())
print(t1.isalnum())
print(t.isalpha())

print(t.isspace())
print(t5.isspace())
print(t.strip(' '))

t= 'Man patinka Coca Cola'
print(t.replace('Coca', 'Pepsi')) #galima ir naikinti tarpus

str = '1111Hello1111'
print(str.strip('1'))

print(ord('a'))
print(chr(101))