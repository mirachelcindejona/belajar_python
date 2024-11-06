# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

student_info = {
   "Alice": {"age": 20, "major": "Computer Science"},
   "Bob": {"age": 21, "major": "Mathematics"},
   "Charlie": {"age": 19, "major": "Physics"}
}

while True:
   input_siswa = input("Masukkan nama siswa untuk melihat data: ")
   if input_siswa in student_info:
      print(f"Umur {input_siswa} adalah {student_info[input_siswa]["age"]} tahun dan Prodi nya adalah {student_info[input_siswa]["major"]}")
      break
   else:
      print(f"{input_siswa} tidak ada di data, ulangi proses!")