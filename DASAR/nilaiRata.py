sumValue = float()
averageValue = float()
num = int(input("Masukkan jumlah data : "))
for x in range(0, num):
    currentValue = int(input("Input data : "))
    sumValue = sumValue+currentValue

averageValue = sumValue / num
print("Nilai rata-ratanya adalah : ", averageValue)