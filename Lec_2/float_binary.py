def float_to_binary_of_val(f, c, a, b):
    eps = 1e-10
    left = a
    right = b

    m = (left + right) / 2.0
    while right - left > eps:
        if f(m) < c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0



def float_to_binary_good(f, c, a, b):
    left = a
    right = b

    m = (left + right) / 2.0
    while left != m and right != m:
        if f(m) < c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0

    return left