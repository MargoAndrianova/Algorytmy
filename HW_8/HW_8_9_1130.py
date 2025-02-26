def sum_digits(x: int) -> int:
    return sum(int(d) for d in str(x))


def compare(x: int, y: int) -> bool:
    w_x = sum_digits(x)
    w_y = sum_digits(y)
    if w_x != w_y:
        return w_x > w_y
    else:
        return str(x) > str(y)


def insertion_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare(arr[j], key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    data = list(range(1, n + 1))

    sorted_data = insertion_sort(data)

    k_position = sorted_data.index(k) + 1
    number_on_k = sorted_data[k - 1]

    print(k_position)
    print(number_on_k)