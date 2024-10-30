# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

# Membuat sebuah list buah
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print("Data buah: ", buah)

# Mengganti item dengan nama "ceri" menjadi "cherry"
print('\n\n-----Mengganti item dengan nama "ceri" menjadi "cherry"-----')
buah[2] = "cherry"
print("Data buah setelah diubah: ", buah)

# Menambahkan item dengan nama dan index yang ditentukan oleh User
print('\n\n-----Menambahkan item dengan nama dan index yang ditentukan oleh User-----')
inputNama = input("Masukkan nama item yang ingin ditambahkan: ")
inputIndex = int(input("Ingin menambahkan pada index ke-? "))
buah.insert(inputIndex, inputNama)
print("Data buah setelah ditambahkan: ", buah)

# Mengurutkan item pada List sesuai dengan abjadnya
print('\n\n-----Mengurutkan item pada List sesuai dengan abjadnya-----')
buah.sort()
print("Data buah setelah diurutkan sesuai dengan abjadnya: ", buah)
