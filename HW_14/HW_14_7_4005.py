class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.top_node = None
        self.back_node = None
        self._size = 0

    def empty(self):
        return self.top_node is None

    def push_front(self, item):
        new_node = Node(item)
        if self.empty():
            self.top_node = new_node
            self.back_node = new_node
        else:
            new_node.next = self.top_node
            self.top_node.prev = new_node
            self.top_node = new_node
        self._size += 1
        return "ok"

    def push_back(self, item):
        new_node = Node(item)
        if self.empty():
            self.top_node = new_node
            self.back_node = new_node
        else:
            new_node.prev = self.back_node
            self.back_node.next = new_node
            self.back_node = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"
        item = self.top_node.item
        self.top_node = self.top_node.next
        if self.top_node is not None:
            self.top_node.prev = None
        else:
            self.back_node = None
        self._size -= 1
        return item

    def pop_back(self):
        if self.empty():
            return "error"
        item = self.back_node.item
        self.back_node = self.back_node.prev
        if self.back_node is not None:
            self.back_node.next = None
        else:
            self.top_node = None
        self._size -= 1
        return item

    def front(self):
        if self.empty():
            return "error"
        return self.top_node.item

    def back(self):
        if self.empty():
            return "error"
        return self.back_node.item

    def clear(self):
        self.top_node = None
        self.back_node = None
        self._size = 0
        return "ok"

    def size(self):
        return self._size

    def exit(self):
        return "bye"

def first_wins(c_1, c_2, total):
    if c_1 == 0 and c_2 == total - 1:
        return True
    if c_2 == 0 and c_1 == total - 1:
        return False
    return c_1 > c_2

if __name__ == "__main__":
    n = int(input().strip())
    cards_first = list(map(int, input().split()))
    cards_second = list(map(int, input().split()))
    deque_1 = Deque()
    deque_2 = Deque()
    for card in cards_first:
        deque_1.push_back(card)
    for card in cards_second:
        deque_2.push_back(card)

    moves = 0
    max_moves = 200000

    while not deque_1.empty() and not deque_2.empty() and moves < max_moves:
        moves += 1
        c1 = deque_1.pop_front()
        c2 = deque_2.pop_front()
        if first_wins(c1, c2, n):
            deque_1.push_back(c1)
            deque_1.push_back(c2)
        else:
            deque_2.push_back(c1)
            deque_2.push_back(c2)

    if moves >= max_moves and not deque_1.empty() and not deque_2.empty():
        print("draw")
    elif deque_1.empty():
        print("second", moves)
    elif deque_2.empty():
        print("first", moves)
