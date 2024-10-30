# Set
a ={"apel", "jeruk", "ceri", "durian"}
b ={"apel", "strawbarry", "bluebarry", "jeruk"}

a.intersection_update(b)
print(a)

d ={"apel", "jeruk", "ceri", "durian"}
e ={"apel", "strawbarry", "bluebarry", "jeruk"}

f = d.intersection(e)
print(f)

a.symmetric_difference_update(b)
print(a)
g = a.symmetric_difference(b)
print(g)

# Dictionary
buah = dict(nama = "Apel", Warna = "Hijau", Manis = True, jumlah = 40)
print(buah)

buah.update({"nama":"Sirsak", "Manis":False})
print(buah)

