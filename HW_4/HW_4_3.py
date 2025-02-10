def f(x):
    return x**3 + x + 1

def binary_search_solution():
    l = 0.0
    h = 10.0
    eps = 1e-7

    while h - l > eps:
        mid = l + (h - l) / 2.0
        if f(mid) > 5:
            h = mid
        else:
            l = mid

    return l

if __name__ == '__main__':
    x = binary_search_solution()
    print(x)
