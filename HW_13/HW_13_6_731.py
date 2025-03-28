class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
    def push(self, item):
        node = Node(item)
        node.next = self.top_node
        self.top_node = node
    def pop(self):
        if self.top_node is None:
            raise Exception("Stack empty")
        item = self.top_node.item
        self.top_node = self.top_node.next
        return item
    def empty(self):
        return self.top_node is None

def prefix_to_infix(prefix_expr: str) -> str:
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    st = Stack()
    # Проходимо по символам виразу справа наліво
    for token in reversed(prefix_expr):
        if token.isalpha():
            st.push((token, 3))
        elif token in prec:
            left_expr, left_prec = st.pop()
            right_expr, right_prec = st.pop()
            op_prec = prec[token]
            if left_prec < op_prec:
                left_expr = "(" + left_expr + ")"
            if right_prec < op_prec or (right_prec == op_prec and token in "-/"):
                right_expr = "(" + right_expr + ")"
            st.push((left_expr + token + right_expr, op_prec))
        else:
            raise Exception
    if st.empty():
        raise Exception
    infix_expr, _ = st.pop()
    if not st.empty():
        raise Exception
    return infix_expr

if __name__ == '__main__':
    f = open("input.txt")
    prefix_expr = f.read().strip()
    f.close()
    try:
        result = prefix_to_infix(prefix_expr)
        print(result)
    except Exception:
        print("Error")
