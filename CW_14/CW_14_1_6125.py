class Queue:
    def __init__(self):
        self.max_size = 100
        self.arr = [0] * self.max_size
        self.front_index = 0
        self.rear_index = 0
        self.count = 0

    def push(self, item):
        self.arr[self.rear_index] = item
        self.rear_index = (self.rear_index + 1) % self.max_size
        self.count += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % self.max_size
        self.count -= 1
        return item

    def front(self):
        if self.empty():
            return "error"
        return self.arr[self.front_index]

    def size(self):
        return self.count

    def clear(self):
        self.front_index = 0
        self.rear_index = 0
        self.count = 0
        return "ok"

    def exit(self):
        return "bye"

    def empty(self):
        return self.count == 0

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
