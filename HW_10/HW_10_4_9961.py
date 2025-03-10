def solve(n, k):
    arr = list(range(1, n + 1))
    product = int(nums) * value
    if product <= max_val:
        return
    elif pieces == 1:
        max_val = product
        return

    if pieces == 1:
        product = int(nums) * value
        if product > max_val:
            max_val = product
        return

    for i in range(1, len(nums) - pieces + 2):
        sub_nums = nums[i:]
        sub_val = int(nums[:i]) * value
        solve(sub_nums, pieces - 1, sub_val)


if __name__ == '__main__':
    n, k = int(input()), int(input())
    solve(n, k)