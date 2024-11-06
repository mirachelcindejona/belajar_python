# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

students = {
   "Alice":"Computer Science",
   "Bob":"Mathematics",
   "Charlie":"Physics",
   "Crlie":"Physics",
   "Carlie":"Physics",
   "Chari":"Physics",
   "Davd":"Computer Science",
   "David":"Computer Science",
   "Ev":"Mathematics",
   "Eva":"Mathematics"
}

# Cara 1
print("=====Cara 1=====")
students_values = list(students.values())

count_cs = students_values.count("Computer Science")
count_mtk = students_values.count("Mathematics")
count_phy = students_values.count("Physics")
x = {
   "Computer Science" : count_cs,
   "Mathematics" : count_mtk,
   "Physics" : count_phy,
}

for prodi, count in x.items():
    print(f"Prodi {prodi} sebanyak {count}")

# Cara 2
print("=====Cara 2=====")
prodi_count = {}

for student, prodi in students.items():
    if prodi in prodi_count:    
        prodi_count[prodi] += 1
    else:
        prodi_count[prodi] = 1

for prodi, count in prodi_count.items():
    print(f"prodi {prodi.lower()} sebanyak {count}")
