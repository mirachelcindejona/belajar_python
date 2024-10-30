# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

# ==========1==========
# List nilai 10 mahasiswa
nilaiMhs = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
print('list nilai 10 mahasiswa: ', nilaiMhs)

# ==========1-A==========
# Nilai maksimum dari nilai mahasiswa
nilaiMax = max(nilaiMhs)
print(f'\nNilai maksimum dari nilai mahasiswa: {nilaiMax}')

# Nilai minimum dari nilai mahasiswa
nilaiMin = min(nilaiMhs)
print(f'Nilai minimum dari nilai mahasiswa: {nilaiMin}')

# Nilai rata-rata dari nilai mahasiswa
nilaiAvg = sum(nilaiMhs) / len(nilaiMhs)
print(f'Nilai rata-rata dari nilai mahasiswa: {nilaiAvg}')

# ==========1-B==========
# Angka terbesar kedua dalam daftar nilai tersebut
nilaiMhs.sort()
nilaiMhs.reverse()
print(f'\nNilai terbesar kedua dalam daftar tersebut adalah {nilaiMhs[1]}, karena jika diurutkan dari yang terbesar yaitu menjadi {nilaiMhs}\n')