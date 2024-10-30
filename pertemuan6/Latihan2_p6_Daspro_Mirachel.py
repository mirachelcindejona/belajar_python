# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

bilangan = int(input("Masukkan bilangan: "))

if (bilangan > 0):
   if(bilangan % 2) == 0:
      print(f"Bilangan tersebut adalah bilangan positif dan termasuk bilangan genap")
   else:
      print(f"Bilangan tersebut adalah bilangan positif dan termasuk bilangan ganjil")
elif (bilangan < 0):
   if(bilangan % 2) == 0:
      print(f"Bilangan tersebut adalah bilangan negatif dan termasuk bilangan genap")
   else:
      print(f"Bilangan tersebut adalah bilangan negatif dan termasuk bilangan ganjil")
else:
   print(f"Bilangan bernilai 0 jadi bilangan tersebut adalah bilangan genap")
