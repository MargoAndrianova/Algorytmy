def generate(target, start, used_mask, current_sum=0, current_mask=0):
    res = []
    if current_sum == target:
        return [current_mask]
    if current_sum > target:
        return []
    for i in range(start, m):
        if used_mask & (1 << i):
            continue
        res.extend(generate(target, i + 1, used_mask, current_sum + bills[i], current_mask | (1 << i)))
    return res

def solve(i, used_mask):
    if i == n:
        return True
    target = salaries[i]
    subsets = generate(target, 0, used_mask)
    for subset in subsets:
        if solve(i + 1, used_mask | subset):
            return True
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    salaries = list(map(int, input().split()))
    bills = list(map(int, input().split()))

    salaries.sort(reverse=True)
    bills.sort(reverse=True)

    print("YES" if solve(0, 0) else "NO")
