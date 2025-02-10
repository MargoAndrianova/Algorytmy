import math

def f(x):
    return math.sin(x) - x/3

def binary_search_solution():
    l = 1.6
    h = 3.0
    eps = 1e-7

    while h - l > eps:
        mid = l + (h - l) / 2.0
        if f(mid) > 0:
            h = mid
        else:
            l = mid
    return l

if __name__ == '__main__':
    x = binary_search_solution()
    print(x)
