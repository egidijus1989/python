# while salyga:
#     veiksmai kol salyga teisinga
#     svarbu ... turi buti keiciama salygos reiksme
# else:
#     ciklas pilnai ivyko...
    
# kiti sakiniai

#atspausdinti skaicius nuo 1 iki n

n = int(input('n=...'))

sk = 1
while sk <= n+1:
    if sk == 13:
        break
    print(sk, end=(', '))
    sk = sk + 1
else:
    print('Ciklas pilnai ivykdytas')
print('programa baigia darba')