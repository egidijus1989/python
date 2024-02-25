# mes turime rgb spalva, ja paversti i hex
# primityvas... is 10-io i 16-aini

def verciam(sk):
    return '%02x' % sk

def verciamTrys(r, g, b):
    # return '%02x' % sk
    return('{:02x}' * 3).format(r, g, b)

print(verciam(25))
print(verciamTrys(255, 158, 3))