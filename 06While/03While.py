#amzinas ivedimas
pasirinkimas = True
while pasirinkimas :
    sk = int(input('sk = ...'))
    atsakymas = input('Ar dar norite ivesti skaiciu (T/N) ')
    if atsakymas != 'T' and atsakymas != 't':
        pasirinkimas = False
        
print('Pagaliau...')