def less_than(x: int, y: int) -> bool:
    # Порівнює два числа за останньою цифрою, а при рівності — за значенням числа.
    if x % 10 != y % 10:
        return x % 10 < y % 10
    return x < y


def insertion_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and less_than(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))

    sorted_numbers = insertion_sort(data)
    print(" ".join(map(str, sorted_numbers)))
