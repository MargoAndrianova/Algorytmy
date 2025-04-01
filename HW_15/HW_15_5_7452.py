class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None

class List:
    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        cur = self.head
        while cur is not None:
            print(cur.data, end = " ")
            cur = cur.next
        print()

    def PrintReverse(self) -> None:
        def rec_print(node: 'Node | None') -> None:
            if node is None:
                return
            rec_print(node.next)
            print(node.data, end = " ")
        rec_print(self.head)
        print()

if __name__ == '__main__':
    n = int(input().strip())
    input_data = list(map(int, input().split()))
    linked_list = List()
    for number in input_data:
        linked_list.addToTail(number)
    linked_list.Print()
    linked_list.PrintReverse()
