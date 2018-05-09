angka = int(input('Masukkan berapa jumlah angka yang ingin dimasukkan : '))
list = []
for jumlah in range(angka):
    list.append(int(input('Masukkan angka ke-%d'% (jumlah+1)+': ')))

print('Angka terbesar adalah %d'% max(list),end=', ')
print('dan angka terkecil adalah %d'% min(list))
print('Rata-ratanya adalah {0:.2f}'.format(sum(list)/float(len(list))))