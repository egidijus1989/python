# duotos 2 duomenu eilutes. Rasti mediana
sar1 = [4, 8, 9, 7, 9]
sar2 = [5, 8, 9, -1, 25, 8, 7, 9]


def surastiMediana(sar):
    sar.sort()
    ilgis = len(sar)
    if ilgis % 2 != 0:
        m0 = sar[ilgis//2]
    else:
        m0 = (sar[ilgis//2] + sar[ilgis//2 -1])/2
    return f'{sar} mediana = {m0}'

print(surastiMediana(sar1))
print(surastiMediana(sar2))
