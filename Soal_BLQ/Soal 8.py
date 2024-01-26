# Deret angka
data = [1, 2, 4, 7, 8, 6, 9]

# Inisialisasi nilai minimal dan maksimal
# Gunakan nilai tak terhingga sebagai inisialisasi minimum
min_sum = float('inf')  
# Gunakan nilai tak terhingga sebagai inisialisasi maksimum
max_sum = float('-inf')  

# Iterasi melalui deret angka
for i in range(len(data) - 3):
     # Hitung penjumlahan 4 komponen saat ini
    current_sum = data[i] + data[i+1] + data[i+2] + data[i+3] 
    
    # Perbarui nilai minimal dan maksimal
    if current_sum < min_sum:
        min_sum = current_sum
    
    if current_sum > max_sum:
        max_sum = current_sum

# Menampilkan hasil
print(f"Nilai minimal penjumlahan 4 komponen: {min_sum}")
print(f"Nilai maksimal penjumlahan 4 komponen: {max_sum}")