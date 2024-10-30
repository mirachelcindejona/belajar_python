# Nama : Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

# Mencari Luas Segitiga
print('-----Mencari Luas Segitiga-----')
alas = int(input('Masukkan Alas : '))
tinggi = int(input('Masukkan Tinggi : '))
luas = alas * tinggi / 2
print(f"Luas segitiga dengan Alas = {alas} dan Tinggi = {tinggi} adalah {luas}" )

# engelompokkan bilangan ganjil dan genap
print('-----Mengelompokkan bilangan ganjil dan genap-----')
bilangan = int(input('Masukkan Angka =  '))
if bilangan % 2 == 0 :
   print('Bilangan ini adalah Genap')
else :
   print('Bilangan ini adalah Ganjil')   

# Mengelompokkan nilai
print('-----Mengelompokkan nilai-----')
nilai = int(input('Masukkan Nilai =  '))
if nilai >= 60 :
   print('Lulus')
else :
   print('Tidal Lulus')   
