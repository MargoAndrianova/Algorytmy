import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data == current.data:
                    return
                elif data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: "Node | None") -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

if __name__ == "__main__":
    bst = BST()
    input_data = input().strip().split()
    for num_str in input_data:
        num = int(num_str)
        if num == 0:
            break
        bst.insert(num)
    print(bst.height())
