def f(x):
    return x**3 + x + 1

def binary_search_real(f, c, left, right, eps=1e-6):
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) < c:
            left = mid
        else:
            right = mid
    return right

result = binary_search_real(f, 5, 0, 10)
print(f"Min x: {result:.5f}")
