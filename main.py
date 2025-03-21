def solve(N: int, min_val: int) -> list[list[int]]:
    if N == 0:
        return [[]]
    res = []
    for i in range(min_val, N+1):
        for j in solve(N-i, i):
            res.append([i] + j)
    return res


if __name__ == '__main__':
    N = int(input())
    for i in solve(N, 1):
        if len(i) == 1:
            continue
        print("+".join(map(str, i)))