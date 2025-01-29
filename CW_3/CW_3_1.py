def solve(n):
    cnt = 0
    while n > 0:
        cnt += n & 1
        n >>= 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    print(solve(n))