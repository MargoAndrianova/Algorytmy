def bsearch(arr, x):
    return _bsearch(arr, 0, len(arr) - 1, x)

def _bsearch(arr, l, r, x):
    if l == r:
        return l
    m = l + (r - l) // 2
    if arr[m] < x:
        return _bsearch(arr, m + 1, r, x)
    else:
        return _bsearch(arr, l, m, x)


if __name__ == '__main__':
    if __name__ == '__main__':
        arr = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9]
        x = 5
        print(bsearch(arr, x))