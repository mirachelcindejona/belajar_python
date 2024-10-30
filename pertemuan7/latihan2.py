# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

a = 0
angka_list = [] 

while True:
   input_angka = int(input("Masukkan angka: "))
   if input_angka < 0:
      break
   a += input_angka
   angka_list.append(str(input_angka)) 

penjumlahan = "+".join(angka_list)

print(f"{penjumlahan} = {a}")