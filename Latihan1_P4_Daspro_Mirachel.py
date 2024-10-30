# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

# Menghapus semua duplikasi dan mengembalikan daftar angka yang hanya berisi elemen unik
numbers = [10,20,20,30,40,50,50,60]
numbers_set = set(numbers)
numbers = list(numbers_set)
numbers.sort()
print(numbers)