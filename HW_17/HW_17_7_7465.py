class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = TreeNode(val)
        else:
            self._insert(self.head, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def same_tree(self, other):
        def is_same(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            return is_same(n1.left, n2.left) and is_same(n1.right, n2.right)
        return 1 if is_same(self.head, other.head) else 0


if __name__ == '__main__':
    n = int(input().strip())
    arr_1 = list(map(int, input().split()))
    m = int(input().strip())
    arr_2 = list(map(int, input().split()))

    tree_1 = Tree()
    for num in arr_1:
        tree_1.insert(num)

    tree_2 = Tree()
    for num in arr_2:
        tree_2.insert(num)

    print(tree_1.same_tree(tree_2))
