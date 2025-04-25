n, m = map(int, input().split())

list_exit = {i: [] for i in range(1, n+1)}
check = True
for i in range(m):
    exit_edge, enter_edge = map(int, input().split())
    if enter_edge not in list_exit[exit_edge]:
        list_exit[exit_edge].append(enter_edge)
    else:
        check = False
        break

print("NO" if check else "YES")


