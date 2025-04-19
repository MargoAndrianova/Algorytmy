n = int(input())
a = list(map(int, input().split()))

is_heap = True
for i in range(n // 2):
    left  = 2*i + 1
    right = 2*i + 2
    if left < n and a[i] > a[left]:
        is_heap = False
        break
    if right < n and a[i] > a[right]:
        is_heap = False
        break

print("YES" if is_heap else "NO")
