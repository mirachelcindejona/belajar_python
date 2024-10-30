"""
Nama: Mirachel Cindejona
NIM: 2401638
Kelas: RPL 1B
"""
# Soal Nomor 2 Aplikasi 2

jumlah_genap = 0
jumlah_ganjil = 0

while True:
    bilangan = int(input("Input bilangan: "))
    
    if bilangan < 0:
        break
        
    if bilangan % 2 == 0:
        jumlah_genap += bilangan
    else:
        jumlah_ganjil += bilangan

print(f"\nJumlah bilangan genap: {jumlah_genap}")
print(f"Jumlah bilangan ganjil: {jumlah_ganjil}")
