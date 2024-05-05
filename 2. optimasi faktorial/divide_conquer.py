import time

batas_dc = 1000

def faktorial_dc(n):
    if n == 0:
        return 1
    elif n <= batas_dc:
        result = n * faktorial_dc(n - 1)
        return result
    else:
        total = 1
        for i in range(1, n + 1):
            total *= i
        return total

n = int(input("Masukkan bilangan bulat non-negatif: "))

start_time = time.time()

if n <= batas_dc:
    hasil_faktorial = faktorial_dc(n)
    algoritma = "Divide and Conquer"
elif n > batas_dc:
    hasil_faktorial = 1
    for i in range(1, n + 1):
        hasil_faktorial *= i
    algoritma = "Standar"

end_time = time.time()

execution_time = end_time - start_time

print(f"Faktorial {n} ({algoritma}) adalah {hasil_faktorial}")
print("Lama eksekusi:", execution_time, "detik")
