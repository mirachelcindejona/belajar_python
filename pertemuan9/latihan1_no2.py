# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

def volume_tabung(jari_jari_lingkaran, tinggi):
    volume = 3.14 * jari_jari_lingkaran**2 * tinggi
    return volume

jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))

tinggi = float(input("Masukkan tinggi tabung: "))

volume = volume_tabung(jari_jari_lingkaran, tinggi)

print(f"Volume tabung adalah: {volume}")

   