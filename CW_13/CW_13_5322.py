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
    binary_str = input().strip()
    num = int(binary_str, 2)

    if num == 0:
        print("0")
    else:
        stack = Stack()
        while num > 0:
            r = num % 16
            num //= 16
            if r < 10:
                digit = str(r)
            else:
                digit = chr(ord('A') + (r - 10))
            stack.push(digit)
        result = ""
        while not stack.empty():
            result += stack.pop()
        print(result)
