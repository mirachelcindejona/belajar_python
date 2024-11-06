# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

def hitung_selisih_waktu():
   print("\n=== Program Menghitung Selisih Waktu ===\n")
   
   # Buat inputan dulu
   print("Input Waktu Mulai:")
   jam_mulai = int(input("Jam: "))
   menit_mulai = int(input("Menit: "))
   detik_mulai = int(input("Detik: "))
   
   print("\nInput Waktu Selesai:")
   jam_selesai = int(input("Jam: "))
   menit_selesai = int(input("Menit: "))
   detik_selesai = int(input("Detik: "))
   
   # Jadiin detik dulu dari yang diinputin
   total_detik_mulai = (jam_mulai * 3600) + (menit_mulai * 60) + detik_mulai
   total_detik_selesai = (jam_selesai * 3600) + (menit_selesai * 60) + detik_selesai
   
   # Hitung selisihnya
   selisih_detik = total_detik_selesai - total_detik_mulai
   
   # Jadiin jam menit detik lagi
   jam = selisih_detik // 3600
   selisih_detik %= 3600
   menit = selisih_detik // 60
   detik = selisih_detik % 60
   
   print("\nSelisih Waktu:")
   print(f"{jam} jam - {menit} menit - {detik} detik\n")

hitung_selisih_waktu()
