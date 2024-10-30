"""
Nama: Mirachel Cindejona
NIM: 2401638
Kelas: RPL 1B
"""
# Soal Nomor 4 Aplikasi 4

nim = int(input("Input 3 digit NIM terakhir : "))

# Rentang NIM: 001 – 050 jika NIM ganjil K1 jika genap K2
if 1 <= nim <= 50:
    if nim % 2 == 1:
        kelas = "K1"
    else:
        kelas = "K2"
# Rentang NIM: 051 – 100 jika NIM ganjil K3 jika genap K4
elif 51 <= nim <= 100:
    if nim % 2 == 1:
        kelas = "K3" 
    else:
        kelas = "K4"
# Rentang NIM: 101 – 150 jika NIM ganjil K5 jika genap K6
elif 101 <= nim <= 150:
    if nim % 2 == 1:
        kelas = "K5"
    else:
        kelas = "K6"
# Rentang NIM: > 151 jika NIM ganjil K7 jika genap K8
elif nim > 151:
    if nim % 2 == 1:
        kelas = "K7"
    else:
        kelas = "K8"
else:
    print("Masukkan NIM dengan benar!")
    kelas = "Tidak ada"

if kelas != "Tidak ada":
   print(f"Silakan masuk ke kelas {kelas}")
