class persegipanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = p

    def ubahpanjang(self, p):
        self.p = p

    def ubahlebar(self, l):
        self.l = l

    def hitungkeliling(self):
        return 2*(self.p+self.l)

    def hitungluas(self):
        return self.p*self.l

    def cetakkeliling(self):
        print('Keliling persegi panjang adalah %d'% self.hitungkeliling())

    def cetakluas(self):
        print('Luas persegi panjang adalah %d'% self.hitungluas())

if __name__ == '__main__':
    obj1 = persegipanjang(5, 4)
    obj1.cetakluas()
    obj1.cetakkeliling()

    obj2 = persegipanjang(10, 5)
    obj2.cetakluas()
    obj2.cetakkeliling()