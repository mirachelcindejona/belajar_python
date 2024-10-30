# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

import datetime

nama = input("Masukkan nama Anda : ")
tahunLahir = int(input("Masukkan tahun lahir Anda : "))
umur = datetime.datetime.now().year - tahunLahir
print(f"Selamat datang {nama}, umur kamu adalah {umur} tahun")