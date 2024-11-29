# Fungsi rekursif untuk menghitung penjumlahan aritmatika
def sum_arithmetic_recursive(a, d, n):
    if n == 1:
        return a
    return a + (n - 1) * d + sum_arithmetic_recursive(a, d, n - 1)

# Fungsi iteratif untuk menghitung penjumlahan aritmatika
def sum_arithmetic_iterative(a, d, n):
    total = 0
    for i in range(n):
        total += a + i * d
    return total

def main():
    # Input dari user
    a = int(input("Masukkan suku pertama (a): "))
    d = int(input("Masukkan selisih antar suku (d): "))
    n = int(input("Masukkan jumlah suku (n): "))

    # Hitung menggunakan metode rekursif
    result_recursive = sum_arithmetic_recursive(a, d, n)
    print(f"Hasil penjumlahan aritmatika secara rekursif: {result_recursive}")

    # Hitung menggunakan metode iteratif
    result_iterative = sum_arithmetic_iterative(a, d, n)
    print(f"Hasil penjumlahan aritmatika secara iteratif: {result_iterative}")

if _name_ == "_main_":
    main()