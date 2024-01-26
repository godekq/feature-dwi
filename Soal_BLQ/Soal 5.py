def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Input jumlah bilangan Fibonacci yang ingin ditampilkan
n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))

# Memanggil fungsi fibonacci
result = fibonacci(n)

# Menampilkan hasil
print(f"{n} bilangan Fibonacci pertama: {result}")