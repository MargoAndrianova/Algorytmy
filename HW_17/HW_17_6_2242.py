class Tree:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None

    def insert(self, letter):
        if letter < self.letter:
            if self.left is None:
                self.left = Tree(letter)
            else:
                self.left.insert(letter)
        elif letter > self.letter:
            if self.right is None:
                self.right = Tree(letter)
            else:
                self.right.insert(letter)

    def preorder(self):
        result = self.letter
        if self.left is not None:
            result += self.left.preorder()
        if self.right is not None:
            result += self.right.preorder()
        return result


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    rounds = []
    for line in lines:
        if line == "*":
            break
        rounds.append(line)

    if not rounds:
        print("")
        exit()

    tree = Tree(rounds[-1])
    for round_str in reversed(rounds[:-1]):
        for letter in round_str:
            tree.insert(letter)

    print(tree.preorder())
