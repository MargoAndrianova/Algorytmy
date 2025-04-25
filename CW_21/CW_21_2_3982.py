n, m = int(input())
matrix = [[0]*n for i in range(n)]

for i in range(m):
    data = list(map(int, input().split()))
    k, neighbors = data[0], data[1:]
    for v in neighbors:
        matrix[i][v-1] = 1

for row in matrix:
    print(' '.join(map(str, row)))
