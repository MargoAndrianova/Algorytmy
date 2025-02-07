"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""

def argument(f, m, l, r, eps):
    return r - l > eps


def value(f, m, l, r, eps):
    return abs(f(r) - f(l)) > eps


def neighbours(f, m, l, r, eps):
    return l != m and r != m


condition = neighbours


def solve(f, c, a, b):
    eps = 1e-10
    left = a
    right = b

    m = (left + right) / 2.0
    while condition(f, m, left, right, eps):
        if f(m) < c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0

    return left


def solve_decreasing(f, c, a, b):
    eps = 1e-10
    left = a
    right = b

    m = (left + right) / 2.0
    while condition(f, m, left, right, eps):
        if f(m) > c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0

    return left
