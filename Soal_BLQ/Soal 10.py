# Input string
input_str = input("input: ")

# Memisahkan input menjadi array kata
arr_in = input_str.split(" ")

new_word = ""

# Iterasi melalui setiap kata
for word in arr_in:
    s = word.strip()
    ns = ""

    # Iterasi melalui setiap karakter dalam kata
    for j in range(len(s)):
        t1, t2, t3 = "", "", ""

        if j == 0:
            t1 = s[j]
            ns += t1
        elif j == len(s) - 1:
            t2 = s[j]
            ns += t2
        else:
            t3 = "*"
            ns += t3

    new_word += " " + ns

# Menampilkan hasil
print(new_word.strip())
