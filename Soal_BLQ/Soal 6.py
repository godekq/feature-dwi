def is_palindrome(word):
    # Menghilangkan spasi dan mengubah huruf menjadi huruf kecil
    clean_word = word.lower().replace(" ", "")
    
    # Membandingkan kata dengan kata yang sudah dibalik
    return clean_word == clean_word[::-1]

# Input kata
input_word = input("Masukkan kata: ")

# Memanggil fungsi is_palindrome
result = is_palindrome(input_word)

# Menampilkan hasil
if result:
    print(f"{input_word} adalah palindrome")
else:
    print(f"{input_word} bukan palindrome")
