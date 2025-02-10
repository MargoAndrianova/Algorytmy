import math

def solve():
    def f(x):
        return x * x + math.sqrt(x)

    C = float(input().strip())
    left = 0.0
    right = max(1.0, math.sqrt(C))
    eps = 1e-7

    while f(right) < C:
        right *= 2

    while right - left > eps:
        mid = (left + right) / 2.0
        if f(mid) < C:
            left = mid
        else:
            right = mid

    print("{:.6f}".format(left))


if __name__ == '__main__':
    solve()
