import re

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    def empty(self):
        return self._top is None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
    def pop(self):
        if self.empty():
            return None
        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item
    def top(self):
        if self.empty():
            return None
        return self._top.item

def precedence(op: str) -> int:
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def tokenize(expr: str) -> list[str]:
    return re.findall(r'\d+|[+\-*/()]', expr)

def to_rpn(expr: str) -> list[str] or None:
    tokens = tokenize(expr)
    output = []
    op_stack = Stack()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in "+-*/":
            while (not op_stack.empty()) and (op_stack.top() != '(') and (precedence(op_stack.top()) >= precedence(token)):
                output.append(op_stack.pop())
            op_stack.push(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while not op_stack.empty() and op_stack.top() != '(':
                output.append(op_stack.pop())
            if op_stack.empty():
                return None
            op_stack.pop()
        else:
            return None
    while not op_stack.empty():
        top = op_stack.pop()
        if top == '(':
            return None
        output.append(top)
    return output

def check_number(num_str: str) -> bool:
    return len(num_str) <= 90 and not num_str.startswith('-')

def apply_op(a_str: str, op: str, b_str: str) -> str or None:
    a = int(a_str)
    b = int(b_str)
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b == 0:
            return None
        res = a // b
    else:
        return None
    if res < 0:
        return None
    res_str = str(res)
    if len(res_str) > 90:
        return None
    return res_str

def eval_rpn(rpn: list[str]) -> str or None:
    val_stack = Stack()
    for token in rpn:
        if token.isdigit():
            val_stack.push(token)
        else:
            b = val_stack.pop()
            a = val_stack.pop()
            if a is None or b is None:
                return None
            res = apply_op(a, token, b)
            if res is None:
                return None
            val_stack.push(res)
    if val_stack._size != 1:
        return None
    return val_stack.pop()

expr = input().strip()
rpn = to_rpn(expr)
if rpn is None:
    print("Error")
else:
    result = eval_rpn(rpn)
    if result is None:
        print("Error")
    else:
        print(result)