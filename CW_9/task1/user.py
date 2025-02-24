"""
Реалізуйте алгоритм сортування злиттям.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    if len(array) <= 1:
        return

    m = len(array) // 2
    left = array[:m]
    right = array[m:]
    sort(left)
    sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


# """
# Реалізуйте швидкий алгоритм сортування QuickSort.
# """
#
# N = 1000000  # Кількість елементів масиву.
#
#
# # Використовується у головній програмі для генерування масиву з випадкових чисел
# # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
# # використовувати значення не більше 10к
# # Для швидких алгоритмів сортування з асимптотикою
# # nlog(n) встановіть значення 1 000 000
#
#
# def sort(array):
#     _sort(array, 0, len(array) - 1)
#
#
# def _sort(array, a, b):
#     if a == b:
#         return
#
#     m = a + (b - a) // 2
#     _sort(array, a, m)
#     _sort(array, m + 1, b)
#
#     left = array[a: m + 1]
#
#     i = 0
#     j = m + 1
#     k = a
#
#     while i < len(left) and j <= b:
#         if left[i] < array[j]:
#             array[k] = left[i]
#             i += 1
#
#         else:
#             array[k] = array[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         array[k] = left[i]
#         i += 1
#         k += 1
#


if __name__ == '__main__':
    arr = [9, 1, -1, 20, 18, 0, -5, 7, 13]
    print(arr)
    sort(arr)
    print(arr)



