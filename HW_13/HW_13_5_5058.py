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
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        if self.empty():
            return "Error: Stack is empty"
        item = self._top.item
        self.top = self._top.next
        self._size -= 1
        return item

if __name__ == "__main__":
    str = input()
    stack = Stack()
    check = True

    for i in range(len(str)):
        if str[i] in "([{":
            stack.push(str[i])
        elif str[i] in ")]}":
            if stack.empty():
                check = False
                break
            if str[i] == "}" and str[i] != "{":
                check = False
                break
            elif str[i] == "]" and str[i] != "[":
                check = False
                break
            elif str[i] == ")" and str[i] != "(":
                check = False
                break
    if check and stack.empty():
        print("yes")
    else:
        print("no")


