def selection_sort(arr: list) -> list:
    """
    Сортування вибором.
    Для кожного індексу i знаходить мінімальний елемент у підмасиві arr[i:]
    і обмінює його з елементом на позиції i.
    :param arr: Список елементів для сортування.
    :return: Відсортований список.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    sorted_data = selection_sort(data)
    print(sorted_data)
