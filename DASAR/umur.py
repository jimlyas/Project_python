nama = input('siapa nama kamu? ')
print('hai '+nama+', ini adalah contoh program python.')

umur = int(input('berapa umur kamu? '))
print('Umur '+nama+' adalah %d'%umur+' tahun.')

if 6<=umur<=12:
    print(nama+' masih anak-anak.')
elif 12<umur<=14:
    print(nama+' masih remaja.')
elif 14<umur<=17:
    print(nama+' masih remaja akhir.')
elif 17<umur<=22:
    print(nama+' sudah punya KTP.')
else:
    print(nama+' sudah tua.')