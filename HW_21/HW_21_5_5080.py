n = int(input())

counter = 0
for i in range(n):
    cnt = 0
    matr = list(map(int, input().split()))
    for m in matr:
        if m == 1:
            cnt += 1
    if cnt == 1:
        counter += 1

print(counter)