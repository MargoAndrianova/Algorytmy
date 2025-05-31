def f(x):
    return x**3 + 4*x**2 + x - 6

def binary_search_neighbors(f, left, right, eps=1e-8):
    while right - left > eps:
        mid = (left + right) / 2
        if abs(f(mid)) < eps:
            return mid
        if f(left) * f(mid) < 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

res = binary_search_neighbors(f, 0, 2)
print(f"Solution: {res:.5f}")
