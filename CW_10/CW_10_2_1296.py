def solve(nums: str, pieces: int, value: int):
    global max_val
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
        sub_val = int(nums[:i])*value
        solve(sub_nums, pieces - 1, sub_val)


if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        n, m = line.split()
        max_val = 0
        solve(n, int(m), 1)
        print(max_val)
    f.close()