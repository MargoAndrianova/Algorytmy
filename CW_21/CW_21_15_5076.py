n, m = map(int, input().split())
ans = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    ans[u] += 1
    ans[v] += 1

if n == 0:
    print("YES")
else:
    k = ans[1]
    check = True
    for i in range(2, n + 1):
        if ans[i] != k:
            check = False
            break
    print("YES" if check else "NO")
