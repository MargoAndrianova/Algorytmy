class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
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

def is_possible(target, n):
    stack = Stack()
    current = 1
    j = 0
    while current <= n:
        stack.push(current)
        while not stack.empty() and stack.top_node.item == target[j]:
            stack.pop()
            j += 1
            if j == n:
                break
        current += 1
    while not stack.empty() and j < n and stack.top_node.item == target[j]:
        stack.pop()
        j += 1
    return j == n

while True:
    n_line = input().strip()
    if n_line == "0":
        break
    n_val = int(n_line)
    while True:
        line = input().strip()
        if line == "0":
            print()
            break
        target = list(map(int, line.split()))
        print("Yes" if is_possible(target, n_val) else "No")
