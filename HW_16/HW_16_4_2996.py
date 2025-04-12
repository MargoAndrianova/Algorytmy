import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, key: int, bribe: int):
        self.key = key
        self.bribe = bribe
        self.children = []
    def add_child(self, child: "Tree"):
        self.children.append(child)

def build_tree(index: int, subordinates, bribes, nodes) -> "Tree":
    node = Tree(index, bribes[index])
    for sub in subordinates[index]:
        if nodes[sub] is None:
            child_node = build_tree(sub, subordinates, bribes, nodes)
            nodes[sub] = child_node
        else:
            child_node = nodes[sub]
        node.add_child(child_node)
    nodes[index] = node
    return node

def minimal_cost(node: "Tree") -> int:
    if not node.children:
        return node.bribe
    return node.bribe + min(minimal_cost(child) for child in node.children)

if __name__ == "__main__":
    data = sys.stdin.read().strip().splitlines()
    if not data:
        sys.exit(0)
    n = int(data[0].strip())
    bribes = [0] * (n + 1)
    subordinates = [[] for _ in range(n + 1)]
    line_idx = 1
    for i in range(1, n + 1):
        parts = data[line_idx].split()
        line_idx += 1
        d_i = int(parts[0])
        k_i = int(parts[1])
        bribes[i] = d_i
        if k_i > 0:
            for j in range(k_i):
                sub_id = int(parts[2 + j])
                subordinates[i].append(sub_id)
    nodes = [None] * (n + 1)
    root = build_tree(1, subordinates, bribes, nodes)
    ans = minimal_cost(root)
    print(ans)
