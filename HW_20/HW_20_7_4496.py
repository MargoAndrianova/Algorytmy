import math

class SegmentTree:
    def __init__(self, array):
        self.n0 = len(array)
        size = 1
        while size < self.n0:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        for i, v in enumerate(array):
            self.tree[size + i] = v
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def update(self, pos, value):
        i = pos + self.size
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]
            i //= 2

    def prefix_count(self, limit):
        if self.tree[1] <= limit:
            return self.n0
        idx = 1
        rem = limit
        while idx < self.size:
            left_sum = self.tree[2*idx]
            if left_sum > rem:
                idx = 2*idx
            else:
                rem -= left_sum
                idx = 2*idx + 1
        return idx - self.size


if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    seg = SegmentTree(weights)

    m = int(input())
    results = []
    for i in range(m):
        parts = input().split()
        t = int(parts[0])
        if t == 1:
            capacity = int(parts[1])
            cnt = seg.prefix_count(capacity)
            results.append(str(cnt))
        else:
            x = int(parts[1]) - 1
            y = int(parts[2])
            seg.update(x, y)

    print('\n'.join(results))
