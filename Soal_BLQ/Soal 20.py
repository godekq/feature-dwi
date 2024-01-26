def suit_game(jarak_awal, suit_A, suit_B):
    posisi_A = posisi_B = 0  # Inisialisasi posisi awal pemain A dan B
    putaran_ke = 0  # Inisialisasi putaran ke-0

    # Looping untuk setiap putaran suit
    while abs(posisi_A - posisi_B) != jarak_awal:
        putaran_ke += 1  # Peningkatan putaran
        langkah_A = suit_A[putaran_ke - 1]  # Suit A pada putaran ke-
        langkah_B = suit_B[putaran_ke - 1]  # Suit B pada putaran ke-

        # Update posisi pemain A
        if langkah_A == 'G':
            posisi_A += 2
        elif langkah_A == 'B':
            posisi_A -= 1

        # Update posisi pemain B
        if langkah_B == 'G':
            posisi_B += 2
        elif langkah_B == 'B':
            posisi_B -= 1

        # Cek jika sudah tidak ada jarak antara A dan B
        if abs(posisi_A - posisi_B) == 0:
            return f"Pemenang: {'A' if langkah_A == 'G' else 'B'} pada putaran ke-{putaran_ke}"

    return "Draw"

if __name__ == "__main__":
    # Input
    jarak_awal = 2
    suit_A = "GGG"
    suit_B = "KKB"

    # Panggil fungsi suit_game
    hasil_game = suit_game(jarak_awal, suit_A, suit_B)

    # Cetak hasil
    print(hasil_game)
