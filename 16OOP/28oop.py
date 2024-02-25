# paveldejimai is keliu klasiu, pavojinga paveldeti su super
# yra dvieju tipu taskai: pradzios ir pabaigos koordinates

class PradziosTaskas():
    def __init__(self, prX, prY):
        self.prX = prX
        self.prY = prY

    def PazymekPrTaska(self):
        return self.prX, self.prY
    
class PabaigosTaskas():
    def __init__(self, pbX, pbY):
        self.pbX = pbX
        self.pbY = pbY

    def PazymekPbTaska(self):
        return self.pbX, self.pbY
    
class Tiese(PradziosTaskas, PabaigosTaskas):
    def __init__(self, prX, prY, pbX, pbY, spalva):
        PradziosTaskas.__init__(self, prX, prY)
        PabaigosTaskas.__init__(self, pbX, pbY)
        self.spalva = spalva

    def breziamTiese(self):
        pr_x, pr_y = self.PazymekPrTaska()
        print(f'Pradzios taskas: ({pr_x}, {pr_y})')
        # cia rasoti tieses brezimas
        print(f'Breziame {self.spalva} linija')
        pb_x, pb_y = self.PazymekPbTaska()
        print(f'Pabaigos taskas: ({pb_x}, {pb_y})')

tiese1 = Tiese(1, 1, 10, 20, 'green')

print(tiese1.__dict__)
tiese1.breziamTiese()