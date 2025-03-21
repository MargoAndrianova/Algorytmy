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

if __name__ == "__main__":
    str = input().strip()
    tokens = str.split()
    stack = Stack()
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a // b)
        else:
            stack.push(int(token))
    print(stack.pop())
