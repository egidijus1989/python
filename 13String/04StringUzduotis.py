slaptazodis = input('Iveskite savo slaptazodi:...')
specialus_symboliai = "!@#$%^&*()-+?_=,<>/"

def kodoValidacija(x):
    ilgis = len(x)
    didziosiosRaides = sum(1 for c in x if c.isupper())
    mazosiosRaides = sum(1 for c in slaptazodis if c.islower())
    skaiciai = sum(1 for c in slaptazodis if c.isnumeric())
    specialusSymboliai = sum(1 for c in slaptazodis if c in specialus_symboliai)
    if ilgis < 12:
        ilgisPranesimas = "Slaptazodis netinkamas, jo ilgis yra per trumpas"
    else:
        ilgisPranesimas = ""
    if didziosiosRaides < 2:
        didziosiosRaidesPranesimas = "Slaptazodis netinkamas, nera bent dvieju didziuju raidziu"
    else:
        didziosiosRaidesPranesimas = ""
    if mazosiosRaides < 2:
        mazosiosRaidesPranesimas = "Slaptazodis netinkamas, nera bent dvieju mazuju raidziu"
    else:
        mazosiosRaidesPranesimas = ""
    if skaiciai < 2:
        skaiciaiPranesimas = "Slaptazodis netinkamas, nera bent dvieju skaiciu"
    else:
        skaiciaiPranesimas = ""
    if specialusSymboliai < 2:
        specialusSymboliaiPranesimas = "Slaptazodis netinkamas, nera bent dvieju specialiuju symboliu"
    else:
        specialusSymboliaiPranesimas = ""
    return ilgisPranesimas, didziosiosRaidesPranesimas, mazosiosRaidesPranesimas, skaiciaiPranesimas, specialusSymboliaiPranesimas

print(kodoValidacija(slaptazodis))