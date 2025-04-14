class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, x: int) -> None:
        self.heap.append(x)
        self._sift_up(len(self.heap) - 1)

    def extract(self) -> int:
        max_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return max_val

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] < self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                break


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    n = int(data[0].strip())
    heap = Heap()
    results = []

    for line in data[1:]:
        parts = line.split()
        if parts[0] == "0":
            heap.insert(int(parts[1]))
        elif parts[0] == "1":
            results.append(str(heap.extract()))

    print("\n".join(results))
