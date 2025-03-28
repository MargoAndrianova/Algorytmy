class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def empty(self):
        return self._top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

if __name__ == "__main__":
    fin = open("input.txt", "r")
    expr = fin.readline().strip()
    stack = Stack()
    valid = True

    for ch in expr:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.empty():
                valid = False
                break
            popped = stack.pop()
            if ch == ")" and popped != "(":
                valid = False
                break
            elif ch == "]" and popped != "[":
                valid = False
                break
            elif ch == "}" and popped != "{":
                valid = False
                break

    if not stack.empty():
        valid = False

    print("yes" if valid else "no")
