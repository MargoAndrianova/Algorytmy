def binary_search(arr, x):

    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        print(f"l: {l}, m:{m}, h: {r}, arr[m]: {arr[m]}")
        if arr[m] < x:
            l = m + 1
        else:
            r = m

    return l

if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9]
    x = 5
    print(binary_search(arr, x))