class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

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
            if node is None: return
            print(" -> " + str(node.data), end="")
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        print(" ")

    def inorder(self):
        def _in(node):
            if node is None: return
            _in(node.left)
            print(" -> " + str(node.data), end="")
            _in(node.right)
        _in(self.root)
        print(" ")

    def postorder(self):
        def _post(node):
            if node is None: return
            _post(node.left)
            _post(node.right)
            print(" -> " + str(node.data), end="")
        _post(self.root)
        print(" ")
    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return

        print("Preorder:", end="")
        self.preorder()

        print("Inorder:", end="")
        self.inorder()

        print("Postorder:", end="")
        self.postorder()

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

if __name__ == "__main__":
    main()