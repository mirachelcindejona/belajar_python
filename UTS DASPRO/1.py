"""
Nama: Mirachel Cindejona
NIM: 2401638
Kelas: RPL 1B
"""
# Soal Nomor 1 Aplikasi 1

login = 3

print(f"Silahkan Login\n")
while login > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == "loginUTS" and password == "rpl2024":
        print(f"\nSelamat datang di aplikasi Prodi RPL!")
        break
    else:
        login -= 1
        if login > 0:
           print(f"\nLogin Salah! Kesempatan Anda {login}x kali lagi.\n") 
        else:
           print(f"\nAnda tidak diperkenankan mengakses aplikasi ini.\n")
