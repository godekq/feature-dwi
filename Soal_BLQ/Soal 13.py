def calculate_angle(hour, minute):
    # Memastikan jam dan menit berada dalam rentang yang benar
    if hour < 0 or hour >= 12 or minute < 0 or minute >= 60:
        return "Waktu tidak valid"

    # Menghitung derajat sudut
    angle = abs(30 * hour - 0.5 * (11 * minute))

    # Menyesuaikan agar sudut selalu kurang dari 180 derajat
    if angle > 180:
        angle = 360 - angle

    return angle

# Contoh penggunaan
angle_1 = calculate_angle(3, 0)    # Jarum jam pada pukul 3:00
angle_2 = calculate_angle(5, 30)   # Jarum jam pada pukul 5:30
angle_3 = calculate_angle(2, 20)   # Jarum jam pada pukul 2:20

# Menampilkan hasil
print(f"Derajat Sudut pada Jam 3:00: {angle_1} derajat")
print(f"Derajat Sudut pada Jam 5:30: {angle_2} derajat")
print(f"Derajat Sudut pada Jam 2:20: {angle_3} derajat")