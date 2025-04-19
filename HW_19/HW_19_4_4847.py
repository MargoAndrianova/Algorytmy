class PriorityQueue:
    def __init__(self):
        self.items = [0]
        self.size = 0
        self.pos = {}

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
        id_i, _ = self.items[i]
        id_j, _ = self.items[j]
        self.pos[id_i] = i
        self.pos[id_j] = j

    def sift_up(self, i):
        while i > 1:
            parent = i // 2
            if self.items[i][1] > self.items[parent][1]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        while 2 * i <= self.size:
            left, right = 2 * i, 2 * i + 1
            best = left
            if right <= self.size and self.items[right][1] > self.items[left][1]:
                best = right
            if self.items[best][1] > self.items[i][1]:
                self.swap(i, best)
                i = best
            else:
                break

    def add(self, id, priority):
        self.size += 1
        self.items.append((id, priority))
        self.pos[id] = self.size
        self.sift_up(self.size)

    def pop(self):
        max_id, max_pr = self.items[1]
        last_id, last_pr = self.items[self.size]
        # замінюємо корінь і прибираємо останній елемент
        self.items[1] = (last_id, last_pr)
        self.pos[last_id] = 1
        self.items.pop()
        del self.pos[max_id]
        self.size -= 1
        if self.size > 0:
            self.sift_down(1)
        return max_id, max_pr

    def change(self, id, new_pr):
        i = self.pos[id]
        _, old_pr = self.items[i]
        self.items[i] = (id, new_pr)
        # якщо пріоритет зріс — sift_up, інакше — sift_down
        if new_pr > old_pr:
            self.sift_up(i)
        else:
            self.sift_down(i)


if __name__ == '__main__':
    pq = PriorityQueue()
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            cmd = parts[0]
            if cmd == 'ADD':
                id, pr = parts[1], int(parts[2])
                pq.add(id, pr)
            elif cmd == 'POP':
                id, pr = pq.pop()
                print(id, pr)
            elif cmd == 'CHANGE':
                id, new_pr = parts[1], int(parts[2])
                pq.change(id, new_pr)