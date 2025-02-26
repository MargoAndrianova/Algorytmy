def insertion_sort(arr: list) -> list:
    """
    Сортування вставкою.
    Для кожного елемента arr[i] знаходить його правильне місце серед елементів arr[0:i] і вставляє його,
    таким чином формуючи відсортовану частину масиву.
    :param arr: Список елементів для сортування.
    :return: Відсортований список.
    """
    if arr == sorted(arr):
        return arr

    n = len(arr)
    for i in range(1, n):
        prav_arr = arr.copy()
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if prav_arr != arr:
            print(*arr)
    return arr

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(arr)
