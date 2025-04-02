class Node:
    def __init__(self, key=None):
        self.mKey = key

    def empty(self):
        return self.mKey is None

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

class Tree(Node):
    def __init__(self, key=None):
        super().__init__(key)
        self.mChildren = []
        self.isEnd = False

    def empty(self):
        return super().empty() and len(self.mChildren) == 0

    def addChild(self, child: "Tree") -> None:
        self.mChildren.append(child)

    def getChild(self, key) -> "Tree | None":
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.mChildren

def insertPhone(root: Tree, phone: str) -> bool:
    node = root
    for i, digit in enumerate(phone):
        child = node.getChild(digit)
        if child is None:
            child = Tree(digit)
            node.addChild(child)
        node = child
        if node.isEnd and i < len(phone) - 1:
            return False
    if node.isEnd or node.getChildren():
        return False
    node.isEnd = True
    return True

if __name__ == "__main__":
    p = int(input().strip())
    for _ in range(p):
        n = int(input().strip())
        compatible = True
        root = Tree()
        for _ in range(n):
            phone = input().strip()
            if not insertPhone(root, phone):
                compatible = False
        print("YES" if compatible else "NO")
