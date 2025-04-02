class Node:
    def __init__(self, data: int):
        self.data = data
        self.parent = None
        self.children = []

class Tree:
    def __init__(self):
        self.nodes = {}
        root = Node(1)
        self.nodes[1] = root

    def addChild(self, parent_id: int, child_id: int) -> None:
        parent_node = self.nodes[parent_id]
        new_node = Node(child_id)
        new_node.parent = parent_node
        parent_node.children.append(new_node)
        self.nodes[child_id] = new_node

    def getLCA(self, a: int, b: int) -> int:
        node_a = self.nodes[a]
        node_b = self.nodes[b]
        ancestors = set()
        while node_a is not None:
            ancestors.add(node_a.data)
            node_a = node_a.parent
        while node_b is not None:
            if node_b.data in ancestors:
                return node_b.data
            node_b = node_b.parent
        return 1

if __name__ == '__main__':
    t = int(input().strip())
    tree = Tree()
    for _ in range(t):
        parts = input().strip().split()
        if parts[0] == "ADD":
            tree.addChild(int(parts[1]), int(parts[2]))
        elif parts[0] == "GET":
            print(tree.getLCA(int(parts[1]), int(parts[2])))
