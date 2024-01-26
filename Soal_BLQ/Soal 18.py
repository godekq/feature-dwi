def hitung_air_diminum(jam_makan, kalori, jam_olahraga_mulai):
    total_air = 0
    jam_olahraga_selesai = 18

    for i in range(len(jam_makan)):
        jam, kalori_makan = jam_makan[i], kalori[i]

        # Hitung selisih waktu antara makan dan olahraga
        selisih_waktu = jam_olahraga_mulai - jam

        # Hitung waktu olahraga dalam jam
        waktu_olahraga = 0.1 * kalori_makan * selisih_waktu / 60

        # Hitung air yang diminum saat berolahraga
        air_berolahraga = waktu_olahraga // 30 * 100

        total_air += air_berolahraga

    # Air yang diminum di akhir olahraga
    total_air += 500

    return total_air

if __name__ == "__main__":
    jam_makan = [9, 13, 15, 17]
    kalori = [30, 20, 50, 80]
    jam_olahraga_mulai = 18

    total_air_diminum = hitung_air_diminum(jam_makan, kalori, jam_olahraga_mulai)

    print(f"Total cc air yang diminum Donna selama berolahraga: {total_air_diminum} cc")
