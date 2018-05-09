baris = 3; kolom = 3
namakolom = ('NIM', 'Nama', 'Kelas')
data = [[None for x in range(baris)]for y in range(kolom)]
for a in range(baris):
    for b in range(kolom):
        data[a][b] = input(namakolom[b]+' dari data ke-%d'%(a+1)+' adalah : ')
    print()
for a in range(baris):
    for b in range(kolom):
        print(data[a][b],end='\t')
    print()