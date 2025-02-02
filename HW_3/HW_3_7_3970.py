def first_bin_search(arr, x):

    l = 0
    r = len(arr) - 1
    result = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            result = mid
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return result

def last_bin_search(arr, x):
    l = 0
    r = len(arr) - 1
    result = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            result = mid
            l = mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return result

if __name__ == '__main__':
    cnt_of_butterflies = int(input())
    num_of_bf = list(map(int, input().split()))
    cnt_of_find = int(input())
    bf_to_find = list(map(int, input().split()))

    for i in range(cnt_of_find):
        first = first_bin_search(num_of_bf, bf_to_find[i])
        if first == -1:
            print(0)
        else:
            last = last_bin_search(num_of_bf, bf_to_find[i])
            print(last - first + 1)