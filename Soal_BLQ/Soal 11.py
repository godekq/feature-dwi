def display_pattern(input_str):
    for char in input_str:
        if char.lower() in "aeiou":
            print(f"***{char.lower()}***")
        else:
            print(f"***{char}***")

# Input string
input_str = input("Input: ")

# Memanggil fungsi display_pattern
display_pattern(input_str)