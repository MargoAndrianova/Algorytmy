def sum_i(n):
    sum = 1
    for i in range(1, n + 1):
        el = 1
        for j in range(i):
            el *= i
        sum *= 1/(1 + el)
    return sum

if __name__ == '__main__':
    print(sum_i(3))