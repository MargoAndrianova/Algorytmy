import sys


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
            self.count += 1
            return
        current = self.root
        while True:
            if data == current.data:
                return
            elif data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    self.count += 1
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    self.count += 1
                    break
                current = current.right

    def find_largest_and_parent(self):
        current = self.root
        parent = None
        while current.right is not None:
            parent = current
            current = current.right
        return current, parent

    def find_second_largest(self) -> int:
        largest, parent = self.find_largest_and_parent()
        if largest.left is not None:
            return self._find_max(largest.left).data
        return parent.data

    def _find_max(self, node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current


if __name__ == "__main__":
    bst = BST()
    input_data = sys.stdin.read().strip().split()
    for num_str in input_data:
        num = int(num_str)
        if num == 0:
            break
        bst.insert(num)
    print(bst.find_second_largest())
