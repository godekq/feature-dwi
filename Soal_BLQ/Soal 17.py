def hitung_gunung_lembah(urutan):
    gunung = lembah = 0
    posisi = 0  # Posisi saat ini dalam perjalanannya

    for langkah in urutan:
        if langkah == 'N':
            posisi += 1
        elif langkah == 'T':
            posisi -= 1

        # Cek apakah telah mencapai puncak atau lembah
        if langkah == 'N' and posisi == 0:
            lembah += 1
        elif langkah == 'T' and posisi == 0:
            gunung += 1

    return gunung, lembah

if __name__ == "__main__":
    urutan_perjalanan = "NNTNNTNTTTTNNTTTNTN"

    gunung, lembah = hitung_gunung_lembah(urutan_perjalanan)

    print(f"Jumlah Gunung: {gunung}")
    print(f"Jumlah Lembah: {lembah}")
