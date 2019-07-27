import cx_Oracle
import sys
# Author : J I M L Y


class atm:
    user = None
    pin = None
    saldo = None
    con = cx_Oracle.connect('jimlyas', 'shafira', 'localhost:1521/XE')
    cur = con.cursor()

    def login(self):
        ch = False
        user = input('Masukkan username anda : ')
        atm.cur.execute('select * from bank')
        for row in atm.cur:
            if user==row[0]:
                print('User ditemukan.')
                atm.pin = int(row[1])
                atm.saldo = int(row[2])
                ch = True
                break

        if ch:
            for a in range(3):
                atm.user = user
                ketik = int(input('Masukkan PIN anda :'))
                if atm.pin==ketik:
                    ch = False
                    break;

            if ch==False:
                atm.menu()
            else:
                print('Akun anda diblokir.')
        else:
            print('User tidak ditemukan')
            sys.exit(0)

    def menu(self):
        print('Pilih transaksi yang ingin anda lakukan :')
        print('1. Cek Saldo\n2. Transfer Uang\n3. Tarik Uang')
        pilih = (int(input()))
        if pilih==1:
            print('Anda memilih transaksi cek saldo.')
            atm.ceksaldo()
        elif pilih==2:
            print('Anda memilih transaksi transfer uang.')
            atm.transfer()
        elif pilih==3:
            print('Anda memilih transaksi tarik uang')
            atm.tarik()
        else:
            print('Anda memilih menu yang salah')
            sys.exit(0)

    def ulang(self):
        ulangi = input('Apakah anda ingin melakukan transaksi lain?(y/n)')
        if ulangi=='y':
            atm.menu()
        else:
            print('Terima kasih.')
            sys.exit(0)

    def ceksaldo(self):
        print('Saldo anda adalah : %d'% atm.saldo+'.')
        atm.ulang()

    def transfer(self):
        tujuan = int(input('Masukkan rekening tujuan :'))
        dikirim = int(input('Masukkan uang yang ingin ditransfer :'))
        if atm.saldo-dikirim>0:
            atm.saldo-=dikirim
            statement = 'update bank set saldo =\''+str(atm.saldo)+'\' where username =\''+str(atm.user)+'\''
            atm.cur.execute(statement)
            atm.con.commit()
            print('Anda berhasil mengirimkan uang ke rekening %d'%tujuan+' sejumlah %d'%dikirim+'.')
        else:
            print('Saldo anda tidak mencukupi.')
        atm.ulang()

    def tarik(self):
        ditarik = int(input('Masukkan jumlah uang yang ingin anda ambil : '))
        if atm.saldo-ditarik>0:
            atm.saldo-=ditarik
            statement = 'update bank set saldo =\'' + str(atm.saldo) + '\' where username =\'' + str(atm.user) + '\''
            atm.cur.execute(statement)
            atm.con.commit()
            print('Anda berhasil mengambil uang sejumlah %d'%ditarik+'.')
            print('Saldo anda sekarang berjumlah : %d'%atm.saldo+'.')
        else:
            print('Saldo anda tidak mencukupi.')
        atm.ulang()


if __name__ == '__main__':
    atm.login()