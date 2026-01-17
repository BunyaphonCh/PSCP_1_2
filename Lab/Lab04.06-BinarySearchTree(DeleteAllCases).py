class BSTNode:
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def insert(self, data):
        data = int(data)
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
            elif data > current.data:
                if current.right is None:
                    current.right = BSTNode(data)
                    return
                current = current.right
            else:
                return
    
    def preorder(self):
        def _pre(node):
            if node is None:
                return
            print(" -> " + str(node.data), end="")
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        print(" ")

    def inorder(self):
        def _in(node):
            if node is None:
                return
            _in(node.left)
            print(" -> " + str(node.data), end="")
            _in(node.right)
        _in(self.root)
        print(' ')
    
    def postorder(self):
        def _post(node):
            if node is None:
                return
            _post(node.left)
            _post(node.right)
            print(" -> " + str(node.data), end="")
        _post(self.root)
        print(' ')
    
    def traverse(self):
        if self.is_empty():
            print('This is an empty binary search tree.')
            return
        print("Preorder:", end='')
        self.preorder()
        print('Inorder:',end='')
        self.inorder()
        print('Postorder:',end='')
        self.postorder()

    def delete(self, data):
        data = int(data)
        exists = False
        current = self.root
        while current is not None:
            if data == current.data:
                exists = True
                break
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        if not exists:
            print('Delete Error, ' + str(data) + ' is not found in Binary Search Tree.')
            return
        self.root = self._delete_node(self.root, data)

    def _delete_node(self, node, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = node.left
            while max_node.right is not None:
                max_node = max_node.right
            node.data = max_node.data
            node.left = self._delete_node(node.left, max_node.data)
        return node
    
def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == 'Done':
            break
        condition, data = text.split(': ')
        if condition == 'I':
            my_bst.insert(int(data))
        elif condition == 'D':
            my_bst.delete(int(data))
        else:
            print('Invalid Condition')
    my_bst.traverse()
main()
