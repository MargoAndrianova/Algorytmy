n = int(input())
ans = []
for i in range(n):
    cnt = 0
    data = list(map(int, input().split()))
    for j in data:
        if j == 1:
            cnt += 1
    ans.append(cnt)

print(*ans)