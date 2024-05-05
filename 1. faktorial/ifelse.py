import time
import sys

sys.set_int_max_str_digits(100000000)
# Menginput nilai n
n = int(input("Masukkan nilai n: "))

# Mencatat waktu awal
start_time = time.time()

# Menghitung faktorial n
if n == 0:
  faktorial = 1
else:
  faktorial = 1
  for i in range(1, n + 1):
    faktorial *= i

# Mencatat waktu akhir
end_time = time.time()

# Menghitung waktu eksekusi
waktu_eksekusi = end_time - start_time

# Menampilkan hasil
print(faktorial)
print(f"Waktu eksekusi: {waktu_eksekusi:.5f} detik")
