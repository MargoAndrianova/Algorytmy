n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    matrix[u-1][v-1] = 1

for row in matrix:
    print(' '.join(map(str, row)))
