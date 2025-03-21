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
    n = int(input())
    for j in range(n):
        str = input().strip()
        stack = Stack()
        check = True
        for ch in str:
            if ch in "([":
                stack.push(ch)
            elif ch in ")]":
                if stack.empty():
                    check = False
                    break
                top = stack.pop()
                if ch == ")" and top != "(":
                    check = False
                    break
                if ch == "]" and top != "[":
                    check = False
                    break
        if not check or not stack.empty():
            print("No")
        else:
            print("Yes")
