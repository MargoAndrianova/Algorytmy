def sort(robots: list[tuple[int, int]]) -> None:
    if len(robots) <= 1:
        return
    m = len(robots) // 2
    left = robots[:m]
    right = robots[m:]
    sort(left)
    sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            robots[k] = left[i]
            i += 1
        else:
            robots[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        robots[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        robots[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    n = int(input())
    robots = []
    for i in range(n):
        robots.append(tuple(map(int, input().split())))
    sort(robots)
    for i in robots:
        print(i[0], i[1])
