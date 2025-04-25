n = int(input())
adj = [list(map(int, input().split())) for i in range(n)]

ed = []
for i in range(n):
    for j in range(i+1, n):
        if adj[i][j] == 1:
            ed.append((i+1, j+1))

for u, v in ed:
    print(u, v)
