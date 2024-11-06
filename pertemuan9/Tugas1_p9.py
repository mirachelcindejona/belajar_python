# Nama: Mirachel Cindejona
# NIM : 2401638
# Kelas : 1B-RPL

def fibonacci(n):
    if n <= 0:
        print("\nJumlah deret harus lebih besar dari 0 !!!\n")
        return
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = int(input("Masukkan jumlah deret Fibonacci yang diinginkan: "))

hasil = fibonacci(n)

if hasil:
   print(f"\nDeret Fibonacci dengan {n} angka: {hasil}\n")