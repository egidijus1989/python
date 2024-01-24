
def datosFormatas(*, diena:int, menuo:str) ->str:
    return f'dabar yra {menuo} men. {diena} diena'

print(datosFormatas(diena = 5, menuo = "spalis"))
print(datosFormatas("Rugsejis", "spalis")) #klaida