class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.head is None:
            return "error"
        result = self.head.item
        self.head = self.head.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        return result

    def front(self):
        if self.head is None:
            return "error"
        return self.head.item

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == "__main__":
    queue = Queue()
    f = open("input.txt")
    for line in f:
        res = queue.execute(line)
        if res is not None:
            print(res)
        if line.strip().split()[0] == "exit":
            break