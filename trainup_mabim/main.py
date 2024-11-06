""" 
-Kondisi awal ada s1 i1 s2 i2 s3 i3 di sisi kiri
-s1 dan i2 naik perahu, lalu s1 mengantarkan i1 ke sisi kanan, lalu i1 turun dari perahu sedangkan s1 balik lagi mengantarkan perahu ke sisi kiri
-setelah s1 mengantarkan perahu dia turun dari perahu 
-kondisinya jadi ada s1 s2 i2 s3 i3 di kiri dan i1 di kanan
-s2 dan i2 naik perahu, lalu s2 mengantarkan i2 ke sisi kanan, lalu i2 turun dari perahu sedangkan s2 balik lagi mengantarkan perahu ke sisi kiri
-setelah s2 mengantarkan perahu dia turun dari perahu
-kondisinya jadi ada s1 s2 s3 i3 di kiri dan i1 i2 di kanan
-s3 dan i3 naik perahu, lalu s3 mengantarkan i3 ke sisi kanan, lalu l3 turun dari perahu sedangkan s3 balik lagi mengantarkan perahu ke sisi kiri
-setelah s3 mengantarkan perahu dia turun dari perahu
-kondisinya jadi ada s1 s2 s3 di kiri dan i1 i2 i3 di kanan
-s1 dan s2 naik perahu, lalu s1 mengantarkan s2 ke sisi kanan, lalu s1 dan s2 turun dari perahu dan i3 naik perahu untuk mengantarkan perahu ke sisi kiri
-kondisinya jadi ada s3 di kiri, s1 i1 s2 i2 di kanan, i3 di perahu
-s3 naik ke perahu bersama i3 menyebrang ke sisi kanan lalu turun dari perahu
-semua pasangan pun sudah berada di sisi kanan
-kondisi akhirnya adalah s1 i1 s2 i2 s3 i3 berada di tujuan yaitu di sisi kanan

"""
def tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu):
    print("\nStatus saat ini:")
    print(f"Sisi kiri  : {', '.join(sisi_kiri) if sisi_kiri else 'Kosong'}")
    print(f"Sisi kanan : {', '.join(sisi_kanan) if sisi_kanan else 'Kosong'}")
    print(f"Perahu     : {', '.join(perahu) if perahu else 'Kosong'}")
    print(f"Posisi Perahu: {posisi_perahu}")
    print("-" * 50)

def main():
    # Input nama pasangan
    print("\n=== PROGRAM SIMULASI PENYEBERANGAN SUNGAI ===")
    print("Masukkan nama-nama pasangan (Suami dan Istri):")
    pasangan = []
    for i in range(3):
        print(f"\nPasangan ke-{i+1}")
        suami = input(f"Masukkan nama Suami {i+1}: ")
        istri = input(f"Masukkan nama Istri {i+1}: ")
        pasangan.append((suami, istri))
    
    # Inisialisasi posisi awal
    sisi_kiri = []
    for s, i in pasangan:
        sisi_kiri.extend([s, i])
    perahu = []
    sisi_kanan = []
    posisi_perahu = "sisi kiri"
    
    print("\nPosisi awal:")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Memilih urutan penyeberangan
    print("\nPilih urutan penyeberangan pasangan:")
    print("Contoh format input:")
    print("Jika ingin urutan: Pasangan 1 -> Pasangan 2 -> Pasangan 3")
    print("Maka input: 1 2 3")
    print("\nPasangan yang tersedia:")
    
    for i, (s, i) in enumerate(pasangan, 1):
        print(f"Pasangan {i}: {s} dan {i}")
    
    while True:
        try:
            urutan_input = input("\nMasukkan urutan (pisahkan dengan spasi, contoh: 1 2 3): ")
            urutan = [int(x)-1 for x in urutan_input.split()]
            
            if len(urutan) != 3:
                print("Error: Harus memasukkan 3 angka!")
                continue
                
            if not all(0 <= x <= 2 for x in urutan):
                print("Error: Angka harus antara 1-3!")
                continue
                
            if len(set(urutan)) != 3:
                print("Error: Tidak boleh ada angka yang sama!")
                continue
                
            break
        except ValueError:
            print("Error: Masukkan angka yang valid!")
    
    print("\nSimulasi penyeberangan dimulai!")
    # Proses penyeberangan
    for idx in urutan:
        suami, istri = pasangan[idx]
        
        # Langkah 1: Suami dan Istri naik perahu
        sisi_kiri.remove(suami)
        sisi_kiri.remove(istri)
        perahu.extend([suami, istri])
        print(f"\n{suami} dan {istri} naik perahu")
        tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
        
        # Langkah 2: Istri turun di sisi kanan, suami kembali
        perahu.remove(istri)
        sisi_kanan.append(istri)
        posisi_perahu = "sisi kanan"
        print(f"{istri} turun di sisi kanan, {suami} kembali")
        tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
        
        # Langkah 3: Suami turun di sisi kiri
        perahu.remove(suami)
        sisi_kiri.append(suami)
        posisi_perahu = "sisi kiri"
        print(f"{suami} turun di sisi kiri")
        tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Penyeberangan terakhir
    s1, i1 = pasangan[urutan[0]]
    s2, i2 = pasangan[urutan[1]]
    s3, i3 = pasangan[urutan[2]]
    
    # Dua suami menyeberang
    sisi_kiri.remove(s1)
    sisi_kiri.remove(s2)
    perahu.extend([s1, s2])
    print(f"\n{s1} dan {s2} naik perahu")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Kedua suami turun, istri ketiga membawa perahu kembali
    perahu.remove(s1)
    perahu.remove(s2)
    sisi_kanan.extend([s1, s2])
    sisi_kanan.remove(i3)
    perahu.append(i3)
    posisi_perahu = "sisi kanan"
    print(f"{s1} dan {s2} turun, {i3} membawa perahu kembali")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Penyeberangan terakhir
    sisi_kiri.remove(s3)
    perahu.append(s3)
    posisi_perahu = "sisi kiri"
    print(f"{s3} naik perahu bersama {i3}")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)
    
    # Semua sampai di tujuan
    perahu.remove(s3)
    perahu.remove(i3)
    sisi_kanan.extend([s3, i3])
    posisi_perahu = "sisi kanan"
    print("\nSemua pasangan telah menyeberang!")
    tampilkan_status(sisi_kiri, perahu, sisi_kanan, posisi_perahu)

if __name__ == "__main__":
    main()