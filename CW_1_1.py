n, x, y = [int(i) for i in input().split()]
x, y = min(x, y), max(x, y)

l = 0
r = (n - 1) * y
while l < r:
    mid = l + (l - r) // 2
    k = mid // x + mid // y
    if k < n - 1:
        l = mid + 1
    else:
        r = mid

print(l + r)