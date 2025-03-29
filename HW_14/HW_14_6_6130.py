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

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == "__main__":
    deque = Deque()
    f = open("input.txt")
    for line in f:
        res = deque.execute(line)
        if res is not None:
            print(res)
        if line.strip().split()[0] == "exit":
            break