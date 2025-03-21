class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.top_node = None # посилання на верхівку стеку
        self._size = 0


    def empty(self):
        return self.top_node is None


    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1
        return "ok"


    def pop(self):
        if self.empty():
            return "error"
        item = self.top_node.item
        self.top_node = self.top_node.next
        self._size -= 1
        return item

    def back(self):
        if self.empty():
            return "error"
        return self.top_node.item

    def clear(self):
        self.top_node = None
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
    stack = Stack()
    fin = open("input.txt", "r")
    for line in fin:
        res = stack.execute(line)
        if res is not None:
            print(res)
        if line.strip().split()[0] == "exit":
            break