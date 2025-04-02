class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        output = []
        while current is not None:
            output.append(str(current.data))
            current = current.next
        print(" ".join(output))

    def PrintReverse(self) -> None:
        def rec_print(node):
            if node is None:
                return []
            return rec_print(node.next) + [str(node.data)]
        print(" ".join(rec_print(self.head)))

n = int(input().strip())
nums = list(map(int, input().split()))
linked_list = List()
for num in nums:
    linked_list.addToTail(num)
linked_list.Print()
linked_list.PrintReverse()
