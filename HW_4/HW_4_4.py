import math

def f(x):
    return math.sin(x) - x/3

def binary_search_by_value(f, left, right, eps=1e-6):
    while True:
        mid = (left + right) / 2
        value = f(mid)
        if abs(value) < eps:
            return mid
        if f(left) * value < 0:
            right = mid
        else:
            left = mid

res = binary_search_by_value(f, 1.6, 3)
print(f"Solution: {res:.5f}")