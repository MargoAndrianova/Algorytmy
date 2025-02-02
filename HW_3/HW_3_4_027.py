def biggest_num(a):
    bin_a = bin(a)[2:]
    max_num = int(bin_a, 2)
    for i in range(1, len(bin_a)):
        helper = bin_a[i:] + bin_a[:i]
        current_val = int(helper, 2)
        if current_val > max_num:
            max_num = current_val
    return max_num


if __name__ == '__main__':
    a = int(input())
    print(biggest_num(a))