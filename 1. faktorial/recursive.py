import time
import sys

sys.setrecursionlimit(100000000)
sys.set_int_max_str_digits(100000000)
def faktorial(n):
  if n == 0:
    return 1
  else:
    return n * faktorial(n - 1)

# Menginput nilai n
n = int(input("Masukkan nilai n: "))

# Mencatat waktu awal
start_time = time.time()

# Menghitung faktorial n
hasil = faktorial(n)

# Mencatat waktu akhir
end_time = time.time()

# Menghitung waktu eksekusi
waktu_eksekusi = end_time - start_time

# Menampilkan hasil
print(f"Nilai faktorial dari {n} adalah {hasil}")
print(f"Waktu eksekusi: {waktu_eksekusi:.5f} detik")
