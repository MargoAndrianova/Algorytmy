def insertion_sort(arr: list) -> list:
    """
    Сортування вставкою.
    Для кожного елемента arr[i] знаходить його правильне місце серед елементів arr[0:i] і вставляє його,
    таким чином формуючи відсортовану частину масиву.
    :param arr: Список елементів для сортування.
    :return: Відсортований список.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    n = int(input())
    data = []
    for i in range(n):
        data.append(input())

    sort = insertion_sort(data)

    for j in sort:
        print(j)
