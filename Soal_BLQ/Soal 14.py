def geser_deret(deret, N):
    N = N % len(deret)  # Jika N lebih besar dari panjang deret, ambil modulus

    # Geser elemen-elemen deret
    deret_geser = deret[N:] + deret[:N]

    return deret_geser

# Contoh penggunaan
deret_awal = [3, 9, 0, 7, 1, 2, 4]

# Geser sejauh N = 3
hasil_1 = geser_deret(deret_awal, 3)
print("N = 3:", hasil_1)

# Geser sejauh N = 1
hasil_2 = geser_deret(deret_awal, 1)
print("N = 1:", hasil_2)
