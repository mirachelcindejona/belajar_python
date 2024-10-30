"""
Nama: Mirachel Cindejona
NIM: 2401638
Kelas: RPL 1B
"""
# Soal Nomor 3 Aplikasi 3

n = int(input("Masukkan nilai N: "))

for i in range(n, 0, -1):
    print(f"{i} bebek kecil berenang")
    print("Menyusuri sungai yang deras")
    print("Induknya mencari kwek kwek kwek")
    if i > 1:
        print(f"Hanya {i-1} ekor yang pulang\n")
    else:
        print("Dan semua bebek kecil pulang, aha!\n")
