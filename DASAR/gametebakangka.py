from random import randint
class tebakangka:
    def tebak():
        acak = randint(1, 100)
        chance = 7
        win = False
        while chance!=0:
            print('Kesempatan anda masih %d ' % chance+' lagi.')
            tebak = int(input('Masukkan angka tebakan anda :'))
            if tebak>acak:
                print('angka tebakan anda lebih besar.')
            elif tebak<acak:
                print('angka tebakan anda lebih kecil.')
            else:
                print('Tebakan anda benar!')
                win = True
                break
            chance -= 1
        return win

    if __name__ == '__main__':
        win = tebak()
        if win:
            print('Selamat anda menang!')
        else:
            print('Maaf anda kalah.')