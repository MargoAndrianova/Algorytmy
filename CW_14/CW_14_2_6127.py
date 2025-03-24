class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0

    def empty(self):
        return self.front_node is None

    def push(self, item):
        new_node = Node(item)
        if self.empty():
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self.front_node.item
        self.front_node = self.front_node.next
        self._size -= 1
        if self.front_node is None:
            self.rear_node = None
        return item

    def front(self):
        if self.empty():
            return "error"
        return self.front_node.item

    def size(self):
        return self._size

    def clear(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

if __name__ == "__main__":
    q = Queue()
    while True:
        command = input().strip()
        if not command:
            continue
        parts = command.split()
        cmd = parts[0]
        if cmd == "push":
            print(q.push(int(parts[1])))
        elif cmd == "pop":
            print(q.pop())
        elif cmd == "front":
            print(q.front())
        elif cmd == "size":
            print(q.size())
        elif cmd == "clear":
            print(q.clear())
        elif cmd == "exit":
            print(q.exit())
            break
