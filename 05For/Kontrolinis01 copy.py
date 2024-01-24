k = float(input('parasykite i koki gyli ikalamas vinis vienu smugiu...'))
n = float(input('parasykite vinies ilgi...'))

for i in range (1, int((n/k)+1)):
    if n - i > 0:
        n = n - k
        print(f'Tuk, {i} smugis, liko {n} centimetru')
    else:
        print('Vinis ikaltas')