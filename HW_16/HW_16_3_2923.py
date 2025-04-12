import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.children = []

    def addChild(self, child: "Tree"):
        self.children.append(child)

with open("input.txt") as f:
    lines = f.read().strip().splitlines()

n = int(lines[0].strip())
nodes = [None] * (n + 1)
parents = [0] * (n + 1)
colors = [0] * (n + 1)

for i in range(1, n + 1):
    p_i, c_i = map(int, lines[i].split())
    parents[i] = p_i
    colors[i] = c_i
    nodes[i] = Tree(i, c_i)

root = None
for i in range(1, n + 1):
    if parents[i] == 0:
        root = nodes[i]
    else:
        nodes[parents[i]].addChild(nodes[i])

distinct_count = [0] * (n + 1)

def DFS(node: Tree) -> set:
    current_set = {node.color}
    for child in node.children:
        child_set = DFS(child)
        if len(current_set) < len(child_set):
            current_set, child_set = child_set, current_set
        current_set |= child_set
    distinct_count[node.id] = len(current_set)
    return current_set

DFS(root)

for i in range(1, n + 1):
    print(distinct_count[i], end=" ")