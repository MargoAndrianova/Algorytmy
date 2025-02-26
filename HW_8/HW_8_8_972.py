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
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    sorted_data = selection_sort(data)
    for i in sorted_data:
        print(*i)
