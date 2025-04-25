import math
from math import *

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = 1 << (int(log2(k - 1)) + 1) if k > 1 else 1
        self.mSize = n
        self.mItems = [0] * (2 * n)
        for i in range(k):
            self.mItems[n + i] = array[i]
        for i in range(n - 1, 0, -1):
            self.mItems[i] = math.gcd(self.mItems[2*i], self.mItems[2*i + 1])

    def update(self, pos, x):
        i = pos + self.mSize
        self.mItems[i] = x
        i //= 2
        while i:
            self.mItems[i] = math.gcd(self.mItems[2*i], self.mItems[2*i + 1])
            i //= 2

    def query(self, left, right):
        res = 0
        l = left + self.mSize
        r = right + self.mSize
        while l <= r:
            if l & 1:
                res = math.gcd(res, self.mItems[l])
                l += 1
            if not (r & 1):
                res = math.gcd(res, self.mItems[r])
                r -= 1
            l //= 2
            r //= 2
        return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    st = SegmentTree(a)

    m = int(input())
    for i in range(m):
        q, l, r = map(int, input().split())
        if q == 1:
            print(st.query(l-1, r-1))
        else:
            st.update(l-1, r)