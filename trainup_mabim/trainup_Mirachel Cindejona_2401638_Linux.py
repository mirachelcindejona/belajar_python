"""
         Nama: Mirachel Cindejona
         Kelompok: 2-Linux
         NIM: 2401638
         Kelas: RPL 1B
"""


def tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu):
    print("\nStatus saat ini:")
    print(f"Sisi kiri  : {sisi_kiri if sisi_kiri else 'Kosong'}")
    print(f"Perahu     : {perahu if perahu else 'Kosong'}")
    print(f"Sisi kanan : {sisi_kanan if sisi_kanan else 'Kosong'}")
    print(f"Posisi Perahu: {posisi_perahu}")
    print("-" * 50)

# Input nama pasangan
print("\n=== PROGRAM SIMULASI PENYEBERANGAN SUNGAI ===")
print("Masukkan nama-nama pasangan (Suami dan Istri):")
pasangan = []
for i in range(3):
    print(f"\nPasangan ke-{i+1}")
    suami = input(f"Masukkan nama Suami {i+1}: ")
    istri = input(f"Masukkan nama Istri {i+1}: ")
    pasangan.append((suami, istri))

# Inisialisasi posisi awal
sisi_kiri = []
for s, i in pasangan:
    sisi_kiri.extend([s, i])
perahu = []
sisi_kanan = []
posisi_perahu = "sisi kiri"

print("\nPosisi awal:")
tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)

print("\nSimulasi penyeberangan dimulai!")

# Proses penyeberangan
for i in range(3):
    suami, istri = pasangan[i]
    
    # Langkah 1: Suami dan Istri naik perahu
    sisi_kiri.remove(suami)
    sisi_kiri.remove(istri)
    perahu.extend([suami, istri])
    print(f"\n{suami} dan {istri} naik perahu")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Langkah 2: Istri turun di sisi kanan, suami kembali
    perahu.remove(istri)
    sisi_kanan.append(istri)
    posisi_perahu = "sisi kanan"
    print(f"{istri} turun di sisi kanan, {suami} kembali")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Langkah 3: Suami turun di sisi kiri
    perahu.remove(suami)
    sisi_kiri.append(suami)
    posisi_perahu = "sisi kiri"
    print(f"{suami} turun di sisi kiri")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)

# Penyeberangan terakhir
s1, i1 = pasangan[0]
s2, i2 = pasangan[1]
s3, i3 = pasangan[2]

# Dua suami menyeberang
sisi_kiri.remove(s1)
sisi_kiri.remove(s2)
perahu.extend([s1, s2])
print(f"\n{s1} dan {s2} naik perahu")
tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)

# Kedua suami turun, istri ketiga membawa perahu kembali
perahu.remove(s1)
perahu.remove(s2)
sisi_kanan.extend([s1, s2])
sisi_kanan.remove(i3)
perahu.append(i3)
posisi_perahu = "sisi kanan"
print(f"{s1} dan {s2} turun, {i3} membawa perahu kembali")
tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)

# Penyeberangan terakhir
sisi_kiri.remove(s3)
perahu.append(s3)
posisi_perahu = "sisi kiri"
print(f"{s3} naik perahu bersama {i3}")
tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)

# Semua sampai di tujuan
perahu.remove(s3)
perahu.remove(i3)
sisi_kanan.extend([s3, i3])
posisi_perahu = "sisi kanan"
print("\nSemua pasangan telah menyeberang!")
tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
