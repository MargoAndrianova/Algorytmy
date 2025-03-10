def solve(i, rem, tracks, memo):
    if i == len(tracks):
        return 0
    if (i, rem) in memo:
        return memo[(i, rem)]
    best = solve(i + 1, rem, tracks, memo)
    if tracks[i] <= rem:
        best = max(best, tracks[i] + solve(i + 1, rem - tracks[i], tracks, memo))
    memo[(i, rem)] = best
    return best

if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        if not line.strip():
            continue
        parts = line.split()
        n = int(parts[0])
        s = int(parts[1])
        tracks = list(map(int, parts[2:2+s]))
        memo = {}
        best_sum = solve(0, n, tracks, memo)
        print("sum:" + str(best_sum))
    f.close()
