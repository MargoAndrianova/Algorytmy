class Heap:
    def __init__(self):
        self.mItems = [0]
        self.mSize = 0

    def swap(self, i, j):
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def insert(self, key):
        self.mSize += 1
        self.mItems.append(key)
        self.siftUp()

    def siftUp(self):
        i = self.mSize
        while i > 1:
            parent = i // 2
            if self.mItems[i] > self.mItems[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def siftDown(self):
        i = 1
        while 2 * i <= self.mSize:
            left = 2 * i
            right = left + 1
            max_child = self.maxChild(left, right)
            if self.mItems[i] < self.mItems[max_child]:
                self.swap(i, max_child)
                i = max_child
            else:
                break

    def maxChild(self, left_child, right_child):
        if right_child > self.mSize:
            return left_child
        else:
            if self.mItems[left_child] >= self.mItems[right_child]:
                return left_child
            else:
                return right_child

    def extract(self):
        maximum = self.mItems[1]
        self.mItems[1] = self.mItems[self.mSize]
        self.mSize -= 1
        self.mItems.pop()
        if self.mSize:
            self.siftDown()
        return maximum

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        commands = f.read().splitlines()

    n_commands = int(commands[0].strip())
    heap = Heap()
    results = []
    for cmd in commands[1:]:
        parts = cmd.split()
        if parts[0] == "0":
            heap.insert(int(parts[1]))
        elif parts[0] == "1":
            results.append(str(heap.extract()))

    print("\n".join(results))