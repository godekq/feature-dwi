from datetime import datetime

def convert_to_24_hour_format(time_string):
    try:
        # Mengonversi string waktu ke objek datetime
        time_obj = datetime.strptime(time_string, "%I:%M:%S %p")

        # Mengonversi objek datetime ke string format 24 jam
        time_24_hour_format = time_obj.strftime("%H:%M:%S")

        return time_24_hour_format
    except ValueError:
        return "Format waktu tidak valid"

# Input dari pengguna
time_string_input = input("Masukkan waktu (HH:MM:SS AM/PM): ")

# Panggil fungsi untuk mengonversi format waktu
result = convert_to_24_hour_format(time_string_input)

# Cetak hasil
print(f"Format waktu 24 jam: {result}")
