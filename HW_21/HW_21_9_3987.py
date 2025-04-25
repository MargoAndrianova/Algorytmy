n, m = map(int, input().split())

list = {i:[] for i in range(1, n+1)}
check = True
for i in range(m):
    exit_edge, enter_edge = map(int, input().split())
    list[exit_edge].append(enter_edge)
    list[enter_edge].append(exit_edge)

for j in list:
    for k in range(1, n + 1):
        if k in list[j] and j != k:
            continue
        elif k not in list[j] and j != k:
            check = False

print("YES" if check else "NO")


