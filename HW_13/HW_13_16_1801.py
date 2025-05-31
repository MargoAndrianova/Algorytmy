PRIO = {
    '+': 1,
    '·': 2,
    'v': 3,
}

class Node:
    def __init__(self, op, left=None, right=None, val=None):
        self.op = op
        self.left = left
        self.right = right
        self.val = val

def parse_expr(s):
    pos = [0]
    def peek():
        return s[pos[0]] if pos[0] < len(s) else None
    def get():
        c = s[pos[0]]
        pos[0] += 1
        return c
    def parse_E():
        left = parse_P()
        if peek() == '+':
            get()
            right = parse_E()
            return Node('+', left, right)
        return left
    def parse_P():
        left = parse_F()
        while True:
            c = peek()
            if c is not None and (c.isalpha() or c == '('):
                right = parse_F()
                left = Node('·', left, right)
            else:
                break
        return left
    def parse_F():
        c = peek()
        if c == '(':
            get()
            inner = parse_E()
            assert get() == ')'
            return inner
        elif c is not None and c.isalpha():
            return Node('v', val=get())
        else:
            raise ValueError("Unknown symbol in F")
    return parse_E()

def to_string(node, parent_op=None, is_right_child=False):
    def prio(op):
        if op is None:
            return -1
        return PRIO[op]
    if node.op == 'v':
        return node.val
    elif node.op == '+':
        s = f"{to_string(node.left, '+', False)}+{to_string(node.right, '+', True)}"
        if parent_op == '·':
            return f"({s})"
        return s
    elif node.op == '·':
        left = to_string(node.left, '·', False)
        right = to_string(node.right, '·', True)
        return f"{left}{right}"

if __name__ == '__main__':
    with open("input.txt", "r") as fin:
        for line in fin:
            s = line.strip()
            if not s:
                continue
            ast = parse_expr(s)
            print(to_string(ast))