n = int(input())
A = [list(map(int, input().split())) for i in range(n)]

check = True
for i in range(n):
    for j in range(n):
        if A[i][i] != 0:
            check = False
            break
        if A[i][j] != A[j][i]:
            check = False
            break

print("YES" if check else "NO")