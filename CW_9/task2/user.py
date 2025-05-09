
"""
Реалізуйте швидкий алгоритм сортування QuickSort.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    _sort(array, 0, len(array) - 1)


def _sort(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b

    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    _sort(array, a, right)
    _sort(array, right + 1, b)



if __name__ == '__main__':
    arr = [9, 1, -1, 20, 18, 0, -5, 7, 13]
    print(arr)
    sort(arr)
    print(arr)
