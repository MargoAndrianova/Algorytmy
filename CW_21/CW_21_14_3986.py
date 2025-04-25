n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

sources = []
sinks = []

for i in range(n):
    out_degree = sum(A[i][j] for j in range(n))
    in_degree = sum(A[j][i] for j in range(n))

    if in_degree == 0:
        sources.append(i + 1)
    if out_degree == 0:
        sinks.append(i + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)
