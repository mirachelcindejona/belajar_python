# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

def rata_rata(*angka):
    total = sum(angka)
    rata2 = total / len(angka)
    return total, rata2

angka = []
while True:
   input_angka = int(input("Masukkan angka (0 untuk selesai): "))

   if input_angka == 0:
      break
   angka.append(input_angka)
      

if len(angka) != 0:
   total, rata2 = rata_rata(*angka)

   print(f"Total: {angka} = {total}")
   print(f"Rata-rata: {total}/{len(angka)} = {rata2}")
else:
   print("Jangan langsung masukin 0 donggg!")
   
