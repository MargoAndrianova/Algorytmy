class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: "Node | None" = None


class List:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None


    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def RotateRight(self, k: int) -> None:
        if self.head is None or k == 0:
            return
        current = self.head
        length = 1
        while current.next is not None:
            current = current.next
            length += 1
        self.tail.next = self.head
        k %= length
        if k == 0:
            self.tail.next = None
            return
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail


    def Print(self) -> None:
        current = self.head
        output = []
        while current:
            output.append(str(current.data))
            current = current.next
        print(" ".join(output))


if __name__ == "__main__":
    n = int(input().strip())
    raws = input().split()
    lst = List()
    for x in raws:
        lst.addToTail(int(x))
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            k = int(line)
        except EOFError:
            break
        lst.RotateRight(k)
        lst.Print()