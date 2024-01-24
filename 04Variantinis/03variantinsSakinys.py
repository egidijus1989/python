#suprogramuoti skaiciuotuva +, -, *, /, ^ - kelimas laipsniu, & - saknies traukimas
import math
a = float(input('pirmas skaicius = '))
veiksmas = input('iveskite matematini veiksma ')
if veiksmas != '&':
    b = float(input('antras skaicius = '))
    
match veiksmas :
    case '+' :
        print(f'{a} {veiksmas} {b} = {a + b}')
    case '-' :
        print(f'{a} {veiksmas} {b} = {a - b}')
    case '+' :
        print(f'{a} {veiksmas} {b} = {a + b}')
    case '*' :
        print(f'{a} {veiksmas} {b} = {a * b}')
    case '/' :
        if b == 0:
            print('dalyba is nulio negalima')
        else:
            print(f'{a} {veiksmas} {b} = {a / b}')
    case '^' :
        print(f'{a} {veiksmas} {b} = {a ** b}')
    case '&' :
        if a < 0 :
            print('saknis is neigiamo skaiciau negalima')
        else:
            print(f'{a} {veiksmas} = {math.sqrt(a)}')
    case _:
        print('ivestas neapibreztas veiksmas')