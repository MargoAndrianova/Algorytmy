def solve(current: list[int]):
    if len(current) == k:
        print(" ".join(map(str, current)))
        return
    for num in range(1, n + 1):
        if num not in current:
            current.append(num)
            solve(current)
            current.pop()

if __name__ == "__main__":
    n, k = map(int, input().split())
    solve([])
