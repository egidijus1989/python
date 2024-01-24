try:
    f = open('data2.txt', 'w')
    f.write('Bele kas')
finally:
    f.close()
    
with open('data2.txt', 'a', encoding='utf=8') as f1:
    f1.write(' tra ta ta')
print('Taratata')