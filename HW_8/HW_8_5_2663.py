def bubble_sort(n, arr: list) -> list:
    """
    Виконує сортування бульбашкою списку.
    :param arr: список чисел для сортування
    :return: відсортований список
    """
    cnt = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                cnt += 1
        if not swapped:
            break
    return cnt


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    print(bubble_sort(n, data))
