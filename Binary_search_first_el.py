def binary_search_first_el(arr, x):
    "Якшо елемента немає, то алгоритм поверне індекс першого ел. після"
    "І обов'язково перевіряти чи не виходить елемент за межі масиву"

    low = 0
    high = len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid

    return low

if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9]
    x = 5
    print(binary_search_first_el(arr, x))