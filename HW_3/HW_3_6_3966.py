def binary_search(arr, x):

    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2

        if arr[m] < x:
            l = m + 1
        else:
            r = m

    if arr[l] == x:
        return l
    else:
        return "No"

if __name__ == '__main__':
    cnt_of_butterflies = int(input())
    num_of_bf = list(map(int, input().split()))
    cnt_of_find = int(input())
    bf_to_find = list(map(int, input().split()))

    for i in range(cnt_of_find):
        binary_search(num_of_bf, bf_to_find[i])