#koks "veikiantis" pazimys  0 < p <= 10
#koks "neveikiantis" pazimys p <= 0 && p >= 11
def ivedimas():
    p = int(input('p = '))
    if not (0 < p <= 10) :
        print('netinkamas balas')
        return ivedimas()
    else :
        return p
    
paz = ivedimas()
print(paz)