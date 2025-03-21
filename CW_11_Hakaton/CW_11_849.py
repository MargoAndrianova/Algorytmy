def solve(n: int, min_val: int) -> list[list[int]]:
    if n == 0:
        return [[]]
    result = []
    for i in range(min_val, n + 1):
        for tail in solve(n - i, i):
            result.append([i] + tail)
    return result

if __name__ == '__main__':
    N = int(input().strip())
    for part in solve(N, 1):
        if len(part) == 1:
            continue
        print("+".join(map(str, part)))
