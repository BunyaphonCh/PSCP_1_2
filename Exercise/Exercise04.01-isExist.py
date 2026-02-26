class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def isExist(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        if data < current.data:
            return self._search_recursive(current.left, data)
        return self._search_recursive(current.right, data)

def main():
    tree = BST()
    
    while True:
        line = input()
        if line == "Done":
            break
        
        clean_val = line.replace("I: ", "")
        val = int(clean_val)
        tree.insert(val)
        
    target = int(input())
    print(tree.isExist(target))

main()