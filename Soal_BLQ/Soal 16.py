def hitung_pembayaran(menu, alergi_ikan):
    total_harga = sum(menu.values())  # Menghitung total harga pesanan
    jumlah_teman = len(menu) - 1  # Mengurangi satu teman karena alergi ikan
    pajak = 0.1  # Pajak 10%
    service = 0.05  # Service 5%

    # Menghitung pajak dan service
    total_pembayaran = total_harga + (total_harga * pajak) + (total_harga * service)

    # Membagi total pembayaran kecuali teman yang alergi ikan
    pembayaran_per_teman = total_pembayaran / jumlah_teman

    # Mengurangkan pembayaran teman yang alergi ikan
    pembayaran_per_teman -= menu[alergi_ikan]

    return pembayaran_per_teman

if __name__ == "__main__":
    # Menu dan harga makanan
    menu_makanan = {
        'Tuna Sandwich': 42,
        'Spaghetti Carbonara': 50,
        'Tea pitcher': 30,
        'Pizza': 70,
        'Salad': 30,
        # tambahkan makanan lainnya sesuai kebutuhan
    }

    alergi_ikan = 'Tuna Sandwich'  # Nama makanan yang mengandung ikan

    # Hitung pembayaran per teman
    pembayaran_teman = hitung_pembayaran(menu_makanan, alergi_ikan)

    # Cetak hasil
    print(f"Setiap teman harus membayar: {round(pembayaran_teman, 2)}")
