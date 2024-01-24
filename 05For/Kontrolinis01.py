k = int(input('parasykite i koki gyli ikalamas vinis vienu smugiu...'))
n = int(input('parasykite vinies ilgi...'))

for i in range (0, n+k, k):
    if n -i > 0:
        print(f'Tuk, {i/k} smugis, liko {n-i} centimetru')
    else:
        print('Vinis ikaltas')