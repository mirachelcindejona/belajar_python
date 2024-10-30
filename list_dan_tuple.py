# List
print("=========================================")
print("----------Contoh tipe data List----------")
a = ["apel", "jeruk", "ceri", "durian", "apel"]
print(a)
print("Tipe datanya adalah ", type(a))
print("Panjang dari list tersebut adalah", len(a))

# Cara Slicing List
print("================================")
print("----------Slicing List----------")
print("Data dari index 1 sampai 3 adalah ", a[1:4])


# Cara menambah List diakhir
print("=================================")
print("----------Menambah List diakhir----------")
a.append("sirsak")
print("List a setelah ditambah:\n" , a)

# Cara menambah List disisipkan
print("=================================")
print("----------Menambah List disisipkan----------")
a.insert(4, "mangga")
print("List a setelah ditambah:\n" , a)

# Cara Menghapus List
print("=================================")
print("----------Menghapus List----------")
a.pop(4)
print("List a setelah dihapus:\n" , a)

# List dengan tipe berbeda
print("=================================")
print("----------List dengan tipe berbeda----------")
c = ["apel", 2, True, 12.4]
print(c)

# Menyatukan item List
print("=================================")
print("----------Menyatukan item List----------")
a.extend(c)
print("Setelah disatukan menjadi:\n", a)

# Tuple
print("==========================================")
print("==========================================")
print("----------Contoh tipe data Tuple----------")
b = ("rambutan", "leci", "kiwi", "lemon", "pepaya")
print(b)
print("Tipe datanya adalah ",type(b))
print("Panjang dari list tersebut adalah", len(b))

# Cara Slicing Tuple
print("================================")
print("----------Slicing Tuple----------")
print("Data dari index 1 sampai 3 adalah ", b[1:4])

# Mengubah Tuple ke bentuk List untuk memodifikasi Tuple
print("================================")
print("----------Mengubah Tuple ke bentuk List untuk memodifikasi Tuple----------")
x = list(b)
x[3] = "semangka"
b = tuple(x)
print("Tuple setelah diubah adalah: \n", b)

# Menyisipkan item Tuple
print("================================")
print("----------Menyisipkan item Tuple----------")
x = list(b)
x.insert(2, "ketupat")
b = tuple(x)
print("Tuple setelah disisipkan adalah: \n", b)

# Menambah item Tuple diakhir
print("================================")
print("----------Menambah item Tuple diakhir----------")
x = list(b)
x.append("tahu")
b = tuple(x)
print("Tuple setelah ditambah diakhir adalah: \n", b)

# Menghapus item Tuple
print("================================")
print("----------Menghapus item Tuple----------")
x = list(b)
x.pop(0)
b = tuple(x)
print("Tuple setelah dihapus indeks ke-0 adalah: \n", b)
