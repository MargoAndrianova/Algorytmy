class Stack:
    """Клас, що реалізує стек за допомогою вбудованого списку."""

    def __init__(self, maxlen=100):
        self._items = []
        self._top = -1

    def push(self, item):
        self._items.append(item)
        self._top += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._items.pop()
        self._top -= 1
        return item

    def back(self):
        if self.empty():
            return "error"
        return self._items[-1]

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()
        self._top = -1
        return "ok"

    def empty(self):
        return len(self._items) == 0

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break