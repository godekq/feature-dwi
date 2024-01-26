def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Menggabungkan dua setengah yang telah diurutkan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menyalin sisa elemen (jika ada) dari setengah kiri
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Menyalin sisa elemen (jika ada) dari setengah kanan
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def print_output(arr):
    print("Output:", end=" ")
    for element in arr:
        print(element, end=" ")

if __name__ == "__main__":
    user_input = input("Input: ")
    arr_in = user_input.split()
    arr_int = [int(x) for x in arr_in]

    # Panggil fungsi merge_sort
    merge_sort(arr_int)

    # Cetak output
    print_output(arr_int)