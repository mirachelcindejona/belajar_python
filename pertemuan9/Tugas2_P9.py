# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

def login():
    password_sistem = "Latihan"
    kesempatan = 3
    
    print("\n====== MENU LOGIN LABORATORIUM KOMPUTER ======")
    print("\nLogin dengan 3 kesempatan")

    username = input("Masukkan username: ")
    
    while kesempatan > 0:
        password = input("Masukkan password: ")
        
        if password == password_sistem:
            print("\nLogin berhasil!")
            print("Selamat datang di Sistem Laboratorium Komputer\n")
            break
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(f"\nPassword salah! Sisa kesempatan: {kesempatan}x lagi")
            else:
                print("\nAnda telah melebihi batas percobaan login!")
                print("Sistem akan keluar...\n")

login()
