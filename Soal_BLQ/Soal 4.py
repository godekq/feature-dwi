def main():
    number = int(input("Panjang data yang akan Ditampilkan : "))

    for x in range(1, number + 1):
        n = 0
        for y in range(1, x + 1):
            if x % y == 0:
                n += 1
        if n == 2:
            print(x, end=" ")

if __name__ == "__main__":
    main()