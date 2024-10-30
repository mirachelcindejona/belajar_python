# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

jml_barang = int(input("Masukkan Jumlah Barang: "))

if ( jml_barang < 100):
   total_harga = jml_barang * 5000
   print(f"Harga per barang adalah Rp. 5000 dan total harga barang adalah Rp. {total_harga}")
elif (jml_barang >= 100 and jml_barang <= 150):
   total_harga = jml_barang * 4000
   print(f"Harga per barang adalah Rp. 4000 dan total harga barang adalah Rp. {total_harga}")
elif (jml_barang > 150):
   total_harga = jml_barang * 2500
   print(f"Harga per barang adalah Rp. 2500 dan total harga barang adalah Rp. {total_harga}")
   