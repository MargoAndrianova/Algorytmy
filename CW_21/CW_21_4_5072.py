n = int(input())
cnt = 0
for i in range(n):
    data = list(map(int, input().split()))
    for j in data:
        if j == 1:
            cnt += 1

print(cnt)