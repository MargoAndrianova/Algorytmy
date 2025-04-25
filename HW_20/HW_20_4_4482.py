import math

class SegmentTree:
    def __init__(self, array):
        n = len(array)
        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n = n2
        self.tmin = [10**18] * (2 * n2)
        self.tmax = [0] * (2 * n2)
        for i, v in enumerate(array):
            self.tmin[n2 + i] = v
            self.tmax[n2 + i] = v
        for i in range(n2 - 1, 0, -1):
            self.tmin[i] = min(self.tmin[2*i], self.tmin[2*i + 1])
            self.tmax[i] = max(self.tmax[2*i], self.tmax[2*i + 1])

    def update(self, pos, val):
        i = pos + self.n
        self.tmin[i] = val
        self.tmax[i] = val
        i //= 2
        while i:
            self.tmin[i] = min(self.tmin[2*i], self.tmin[2*i + 1])
            self.tmax[i] = max(self.tmax[2*i], self.tmax[2*i + 1])
            i //= 2

    def query_min_max(self, left, right):
        l = left + self.n
        r = right + self.n
        cur_min = 10**18
        cur_max = 0
        while l <= r:
            if l & 1:
                cur_min = min(cur_min, self.tmin[l])
                cur_max = max(cur_max, self.tmax[l])
                l += 1
            if not (r & 1):
                cur_min = min(cur_min, self.tmin[r])
                cur_max = max(cur_max, self.tmax[r])
                r -= 1
            l //= 2
            r //= 2
        return cur_min, cur_max


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    seg = SegmentTree(a)

    m = int(input())
    for i in range(m):
        q, l, r = map(int, input().split())
        if q == 1:
            mn, mx = seg.query_min_max(l-1, r-1)
            if mn == mx:
                print("draw")
            else:
                print("wins")
        else:
            seg.update(l-1, r)
