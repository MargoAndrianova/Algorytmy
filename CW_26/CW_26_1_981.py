class PQElement:
    def __init__(self, key=None, priority=float('inf')):
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        self.mPriority = priority

    def key(self):
        return self.mKey

    def __lt__(self, other):
        return self.mPriority < other.mPriority

    def __str__(self):
        return f"(item: {self.mKey}, priority: {self.mPriority})"


class PriorityQueue:
    def __init__(self):
        self.mItems = [None]
        self.mElementsMap = {}

    def empty(self):
        return len(self.mItems) == 1

    def insert(self, key, priority):
        if key in self.mElementsMap:
            self.updatePriority(key, priority)
        else:
            el = PQElement(key, priority)
            self.mItems.append(el)
            idx = len(self.mItems) - 1
            self.mElementsMap[key] = idx
            self._siftUp(idx)

    def extractMinimum(self):
        root = self.mItems[1].mKey
        last = self.mItems.pop()
        del self.mElementsMap[root]
        if len(self.mItems) > 1:
            self.mItems[1] = last
            self.mElementsMap[last.mKey] = 1
            self._siftDown(1)
        return root

    def updatePriority(self, key, priority):
        idx = self.mElementsMap.get(key)
        if idx is None:
            return False
        el = self.mItems[idx]
        if priority < el.mPriority:
            el.updatePriority(priority)
            self._siftUp(idx)
        return True

    def _siftUp(self, i):
        while i > 1:
            p = i // 2
            if self.mItems[i] < self.mItems[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _siftDown(self, i):
        n = len(self.mItems) - 1
        while 2*i <= n:
            left = 2*i
            right = left + 1
            smallest = left
            if right <= n and self.mItems[right] < self.mItems[left]:
                smallest = right
            if self.mItems[smallest] < self.mItems[i]:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def _swap(self, i, j):
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]
        self.mElementsMap[self.mItems[i].mKey] = i
        self.mElementsMap[self.mItems[j].mKey] = j


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

visited = [False] * (n+1)
key = [float('inf')] * (n+1)

pq = PriorityQueue()
start = 1
key[start] = 0
for v in range(1, n+1):
    pq.insert(v, key[v])

mst_weight = 0

while not pq.empty():
    u = pq.extractMinimum()
    if key[u] == float('inf'):
        break
    visited[u] = True
    mst_weight += key[u]
    for v, w in adj[u]:
        if not visited[v] and w < key[v]:
            key[v] = w
            pq.updatePriority(v, w)

print(mst_weight)
