import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: "Node | None" = None
        self.right: "Node | None" = None

class BST:
    def __init__(self):
        self.root: "Node | None" = None
        self.count: int = 0

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


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split()
    bst = BST()
    for num_str in input_data:
        num = int(num_str)
        if num == 0:
            break
        bst.insert(num)
    print(bst.count)
