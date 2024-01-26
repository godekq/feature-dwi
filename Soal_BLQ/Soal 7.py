from statistics import mean, median
from collections import Counter

# Deret angka
data = [8, 7, 0, 2, 7, 1, 7, 6, 3, 0, 7, 1, 3, 4, 6, 1, 6, 4, 3]

# Mean
mean_value = mean(data)
print(f"Mean: {mean_value}")

# Median
median_value = median(data)
print(f"Median: {median_value}")

# Modus
counter = Counter(data)
modus = counter.most_common()

# Menentukan modus (jika ada lebih dari satu modus)
if len(modus) > 1 and modus[0][1] == modus[1][1]:
    min_mode = min(modus[0][0], modus[1][0])
    print(f"Modus: {min_mode}")
else:
    print(f"Modus: {modus[0][0]}")
