import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: "Node | None" = None
        self.right: "Node | None" = None

class BST:
    def __init__(self):
        self.root: "Node | None" = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
            return
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

    def inorder_leaves(self) -> list[int]:
        result = []
        stack = []
        current = self.root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.left is None and current.right is None:
                result.append(current.data)
            current = current.right
        return result


if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    bst = BST()
    for token in input_data:
        num = int(token)
        if num == 0:
            break
        bst.insert(num)
    leaves = bst.inorder_leaves()
    print(" ".join(map(str, leaves)))
