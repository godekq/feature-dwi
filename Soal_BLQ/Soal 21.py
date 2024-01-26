def urutan_walk_jump(lintasan):
    st = 0  # Stamina awal
    hasil = []  # Inisialisasi hasil urutan langkah

    for i, elemen in enumerate(lintasan):
        # Jika player berada di lubang, cek apakah memiliki cukup ST untuk melompat
        if elemen == 'O':
            if st < 2:
                return "FAILED"  # Tidak cukup ST untuk melompat, hasilnya "FAILED"
            else:
                st -= 2  # Kurangi ST untuk melompat
                hasil.append('J')  # Tambahkan langkah Jump ke hasil
        else:
            st += 1  # Tambahkan ST untuk berjalan
            hasil.append('W')  # Tambahkan langkah Walk ke hasil

    return hasil

if __name__ == "__main__":
    # Contoh 1
    lintasan1 = "☺____O___Finish"
    hasil1 = urutan_walk_jump(lintasan1)
    print(f"Lintasan 1: {hasil1}")

    # Contoh 2
    lintasan2 = "☺O___O___Finish"
    hasil2 = urutan_walk_jump(lintasan2)
    print(f"Lintasan 2: {hasil2}")
