class Heap:
    def __init__(self):
        self.mItems = [0]
        self.mSize = 0

    def insert(self, key):
        self.mSize += 1
        self.mItems.append(key)
        self._sift_up(self.mSize)

    def extract_min(self):
        root = self.mItems[1]
        self.mItems[1] = self.mItems[self.mSize]
        self.mItems.pop()
        self.mSize -= 1
        if self.mSize > 0:
            self._sift_down(1)
        return root

    def empty(self):
        return self.mSize == 0

    def _sift_up(self, i):
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.mItems[i], self.mItems[parent] = self.mItems[parent], self.mItems[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        while 2*i <= self.mSize:
            left, right = 2*i, 2*i+1
            best = left
            if right <= self.mSize and self.mItems[right] < self.mItems[left]:
                best = right
            if self.mItems[best] < self.mItems[i]:
                self.mItems[i], self.mItems[best] = self.mItems[best], self.mItems[i]
                i = best
            else:
                break


if __name__ == "__main__":
    n = int(input())
    l = [0]*(n+1)
    r = [0]*(n+1)
    for i in range(1, n+1):
        li, ri = map(int, input().split())
        l[i], r[i] = li, ri

    pot = [0]*(n+1)
    for i in range(n, 0, -1):
        if l[i] == -1 or r[i] == -1:
            pot[i] = 0
        else:
            pot[i] = 1 + min(pot[l[i]], pot[r[i]])

    heap = Heap()
    for i in range(1, n+1):
        if r[i] != -1 and l[i] == -1:
            heap.insert(i)
        elif l[i] != -1 and r[i] != -1 and pot[l[i]] < pot[r[i]]:
            heap.insert(i)

    print(heap.extract_min() if not heap.empty() else -1)
