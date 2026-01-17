class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = BSTNode(data)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(data)
                    return
                current = current.right

    def preorder(self):
        def _pre(node):
            if node is None:
                return
            print(" -> " + str(node.data), end="")
            _pre(node.left)
            _pre(node.right)

        _pre(self.root)
        print()


def main():
    bst = BST()
    n = int(input())
    i = 0
    while i < n:
        bst.insert(int(input()))
        i += 1

    print("Preorder:", end="")
    bst.preorder()


main()