# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

print("""
Syarat untuk menjadi model catwalk:
1. Wanita/pria berumur 18-25 tahun
2. Memiliki pengetahuan luas dengan memiliki IQ minimal 130
3. Tinggi badan minimal 170 (Wanita), dan minimal 175 (pria)
""")

jenis_kelamin = input("Masukkan Jenis Kelamin [Wanita/Pria]: ").lower()
if(jenis_kelamin == "wanita"):
   umur = int(input("Masukkan Umur(Dalam Tahun): "))
   if (umur >= 18 and umur <= 25):
      iq = int(input("Masukkan IQ: "))
      if (iq >= 130):
         tinggi_badan = int(input("Masukkan Tinggi Badan: "))
         if(tinggi_badan >= 170):
            print("Selamat Anda dapat menjadi model catwalk Wanita!")
         else:
            print("Maaf tinggi badan Anda tidak mencukupi, Anda memenuhi syarat pertama dan kedua tetapi tidak memenuhi syarat ketiga!")
      else:
         print("Maaf IQ Anda tidak mencukupi, Anda memenuhi syarat pertama tetapi tidak memenuhi syarat kedua!")
   else:
      print("Maaf umur Anda tidak memasuki kriteria, Jadi tidak memenuhi syarat pertama!")
elif(jenis_kelamin == "pria"):
   umur = int(input("Masukkan Umur(Dalam Tahun): "))
   if (umur >= 18 and umur <= 25):
      iq = int(input("Masukkan IQ: "))
      if (iq >= 130):
         tinggi_badan = int(input("Masukkan Tinggi Badan: "))
         if(tinggi_badan >= 175):
            print("Selamat Anda dapat menjadi model catwalk Pria!")
         else:
            print("Maaf tinggi badan Anda tidak mencukupi, Anda memenuhi syarat pertama dan kedua tetapi tidak memenuhi syarat ketiga!")
      else:
         print("Maaf IQ Anda tidak mencukupi, Anda memenuhi syarat pertama tetapi tidak memenuhi syarat kedua!")
   else:
      print("Maaf umur Anda tidak memasuki kriteria, Jadi tidak memenuhi syarat pertama!")
else:
   print("Masukkan jenis kelamin dengan benar!")
