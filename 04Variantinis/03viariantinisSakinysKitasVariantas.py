# Suprogramuoti skaiciuotuva.
# Veiksmai (+, -, *, /, ^ yra kelimas laipsniu, & yra saknies traukimas) [skaicius operacija skaicius]
import math
skaicius_1 = float(input("Skaicius: "))
operacija = input("Operacija: ")
if operacija != "&":
    skaicius_2 = float(input("Skaicius: "))
pavyko = True
rez = "???"
match operacija:
    case "+":
        rez = skaicius_1 + skaicius_2
    case "-":
        rez = skaicius_1 - skaicius_2
    case "*":
        rez = skaicius_1 * skaicius_2
    case "/":
        if skaicius_2 == 0:
            pavyko = False
        else:
            rez = skaicius_1 / skaicius_2
    case "^":
        rez = math.pow(skaicius_1, skaicius_2)
    case "&":
        rez = math.sqrt(skaicius_1)
    case _:
        pavyko = False
if operacija == "&":
    print(f"{skaicius_1} {operacija} = {rez}")
else:
    if pavyko == False:
        print(f"Operacija nepavyko: ", end="")
    print(f"{skaicius_1} {operacija} {skaicius_2} = {rez}")