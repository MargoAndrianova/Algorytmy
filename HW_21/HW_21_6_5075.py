n, m = map(int, input().split())

list_exit = {i: 0 for i in range(1, n+1)}
list_enter = {i: 0 for i in range(1, n+1)}

for i in range(m):
    exit_edge, enter_edge = map(int, input().split())
    list_exit[exit_edge] += 1
    list_enter[enter_edge] += 1

for j in range(1, n + 1):
    print(list_enter[j], list_exit[j])


