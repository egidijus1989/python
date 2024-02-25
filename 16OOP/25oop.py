# mes turime rgb spalva, ja paversti i hex
#permamtomumas === sesioliktainis
# primityvas... is 10-io i 16-aini

# def verciam(sk):
#     return '%02x' % sk

# def verciamTrys(r, g, b):
#     # return '%02x' % sk
#     return('#{:02x}' * 3).format(r, g, b)

# print(verciam(25))
# print(verciamTrys(255, 158, 3))

class Colors:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def toHex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)
    
gray = Colors(80, 80, 80)
print(gray.__dict__)
print(gray.toHex())

class ColorsAlpha(Colors):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.alpha = alpha

    def _alphaToHex(self):
        return f'{int(self.alpha*255):02x}'

    def toHexAlpha(self):
        return f'{super().toHex()}{self._alphaToHex()}'
    
    def rezultatas(self):
        return f'Spalva: {self.toHexAlpha()}'
    
grayA = ColorsAlpha(80, 80, 80, 0.5)
print(grayA.__dict__)
print(grayA.rezultatas())