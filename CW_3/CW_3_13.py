def binary_search(arr, x):

    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l + 1) // 2
        print(f"l: {l}, m:{m}, h: {r}, arr[m]: {arr[m]}")
        if arr[m] < x:
            r = m - 1
        else:
            l = m

    return l

if __name__ == '__main__':
    arr = [9, 8, 8, 8, 7, 6, 5, 5, 4, 3, 2, 2, 1, 1, 1, 0]
    x = 9
    print(binary_search(arr, x))