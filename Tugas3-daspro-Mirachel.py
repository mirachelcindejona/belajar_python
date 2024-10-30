# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

# Menyisipkan item Tuple (insert)
print("===================================================")
print("----------Menyisipkan item Tuple (insert)----------")
a = ("kunci", "lemari", "meja", "kursi", "komputer")
print("Data tuple a = ", a)
x = list(a)
x.insert(2, "papan tulis")
a = tuple(x)
print('Data Tuple setelah disisipkan "papan tulis" di indeks ke-2 adalah: \n', a)

# Menambah item Tuple diakhir (append)
print("========================================================")
print("----------Menambah item Tuple diakhir (append)----------")
b = ("kelinci", "kucing", "sapi", "tikus", "zebra")
print("Data tuple b = ", b)
y = list(b)
y.append("Rusa")
b = tuple(y)
print('Data Tuple setelah ditambah "Rusa" diakhir adalah: \n', b)

# Menghapus item Tuple (pop)
print("==============================================")
print("----------Menghapus item Tuple (pop)----------")
c = ("semangka", "lemon", "melon", "sirsak", "jambu")
print("Data tuple c = ", c)
z = list(c)
z.pop(0)
c = tuple(z)
print("Data Tuple setelah dihapus indeks ke-0 adalah: \n", c)