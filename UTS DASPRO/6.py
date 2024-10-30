"""
Nama: Mirachel Cindejona
NIM: 2401638
Kelas: RPL 1B
"""
# Soal Nomor 6 Aplikasi 6

jml_prima = 0
n = int(input("Masukkan Nilai N = "))

for i in range(1, (n+1)):
   bilangan = int(input(f"Masukkan bilangan ke-{i} = "))
   
   if bilangan > 1:
      prima = True
      for j in range(2, bilangan):
         if bilangan % j == 0:
            prima = False
            break
      if prima:
         jml_prima += bilangan

if jml_prima != 0:
   print(f"\nJumlah bilangan prima adalah {jml_prima}")
else:
   print(f"\nTidak ada item list yang bilangan prima")
