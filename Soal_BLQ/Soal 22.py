def fibonacci_candles(array_input):
    result = 0
    array_fibonacci = [1, 1, 2, 3, 5, 8, 13]
    temp = [array_input[i] - array_fibonacci[i] for i in range(len(array_input))]

    for i in range(len(temp)):
        if temp[i] <= 0:
            result = array_input[i]

    return result

if __name__ == "__main__":
    input_array = [3, 3, 9, 6, 7, 8, 23]

    # Panggil fungsi fibonacci_candles
    hasil = fibonacci_candles(input_array)

    # Cetak hasil
    print(hasil)
