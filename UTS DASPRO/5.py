"""
Nama: Mirachel Cindejona
NIM: 2401638
Kelas: RPL 1B
"""
# Soal Nomor 5 Aplikasi 5

jumlah = 0
bilangan_awal = int(input("Input bilangan : "))
total_tidak_membesar = 0

while total_tidak_membesar < 3:
    bilangan = int(input("Input bilangan : "))
    
    if bilangan > bilangan_awal:
        jumlah += bilangan
        bilangan_awal = bilangan
        total_tidak_membesar = 0
    else:
        total_tidak_membesar += 1
        bilangan_awal = bilangan

print(f"\nHasil penjumlahan nilai yang membesar : {jumlah}")
