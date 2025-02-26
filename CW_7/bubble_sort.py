def bubble_sort(arr: list) -> list:
    """
    Виконує сортування бульбашкою списку.
    :param arr: список чисел для сортування
    :return: відсортований список
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr