# nuo - begalybes iki 0 netinkamas balas
# nuo 1 iki 3 blogas balas
# nuo 4 iki 6 patenkinamas
# nuo 7 iki 9 geras
# 10 labai geras
# nuo 11 iki begalybes netinkamas balas
paz = int(input('pazimys = '))

def pazimys(x):
    if paz <= 0:
        print('netinkamas balas')
    elif 1 <= paz <= 3:
        print('blogas balas')
    elif 4 <= paz <= 6:
        print('patenkinamas balas')
    elif 7 <= paz <= 9:
        print('geras balas')
    elif   paz == 10:
        print('labai geras balas')
    else:
        print('netinkamas balas')
        
print(pazimys(paz))