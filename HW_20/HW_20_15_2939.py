class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (4 * self.n)
        self.lazy = [None] * (4 * self.n)
        self.build(1, 0, self.n - 1, array)

    def build(self, node, l, r, array):
        if l == r:
            self.tree[node] = array[l]
        else:
            mid = (l + r) // 2
            self.build(node * 2, l, mid, array)
            self.build(node * 2 + 1, mid + 1, r, array)
            self.tree[node] = self.tree[node*2] + self.tree[node*2 + 1]

    def apply(self, node, l, r, val):
        self.tree[node] = val * (r - l + 1)
        self.lazy[node] = val

    def push(self, node, l, r):
        if self.lazy[node] is not None and l != r:
            mid = (l + r) // 2
            self.apply(node * 2, l, mid, self.lazy[node])
            self.apply(node * 2 + 1, mid + 1, r, self.lazy[node])
            self.lazy[node] = None

    def update(self, node, l, r, ql, qr, val):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.apply(node, l, r, val)
            return
        self.push(node, l, r)
        mid = (l + r) // 2
        self.update(node * 2, l, mid, ql, qr, val)
        self.update(node * 2 + 1, mid + 1, r, ql, qr, val)
        self.tree[node] = self.tree[node*2] + self.tree[node*2 + 1]

    def query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        self.push(node, l, r)
        mid = (l + r) // 2
        left_sum = self.query(node * 2, l, mid, ql, qr)
        right_sum = self.query(node * 2 + 1, mid + 1, r, ql, qr)
        return left_sum + right_sum

    def range_assign(self, left, right, value):
        self.update(1, 0, self.n - 1, left, right, value)

    def range_sum(self, left, right):
        return self.query(1, 0, self.n - 1, left, right)


if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    st = SegmentTree(arr)

    for i in range(q):
        parts = input().split()
        if parts[0] == '?':
            f = int(parts[1]) - 1
            t = int(parts[2]) - 1
            print(st.range_sum(f, t))
        else:
            i = int(parts[1]) - 1
            j = int(parts[2]) - 1
            d = int(parts[3])
            st.range_assign(i, j, d)
