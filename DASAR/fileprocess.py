class fileprocess:
    def buatfile():
        try:
            nama = input('Masukkan nama file ingin dibuat : ')
            f = open(nama+'.txt', 'w')
            pesan = input('Masukkan pesan anda ke dalam file :\n')
            f.write(pesan)
        finally:
            f.close()

    def bacafile():
        try:
            nama = input('Masukkan nama file yang ingin dibaca : ')
            f = open(nama+'.txt','r')
            lines = f.readlines()
            for line in lines:
                print(line,end='\n')
        finally:
            f.close()

    if __name__ == '__main__':
        bacafile()