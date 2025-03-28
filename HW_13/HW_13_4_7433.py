class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.top_node is None:
            return None
        item = self.top_node.item
        self.top_node = self.top_node.next
        return item

    def empty(self):
        return self.top_node is None

A_str = input().strip()
P_str = input().strip()

try:
    A = int(A_str)
    P = int(P_str)
except:
    print("Error")
    exit()

if A < 0 or P <= 1:
    print("Error")
elif A == 0:
    print("0")
else:
    st = Stack()
    while A > 0:
        rem = A % P
        A //= P
        st.push(rem)
    result = ""
    while not st.empty():
        digit = st.pop()
        if digit < 10:
            result += str(digit)
        else:
            result += "[" + str(digit) + "]"
    print(result)
