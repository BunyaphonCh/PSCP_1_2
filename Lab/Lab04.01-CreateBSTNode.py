class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def main():
    data_input = int(input())
    p_new = BSTNode(data_input)
    print(p_new.data)
    print(p_new.left)
    print(p_new.right)

if __name__ == '__main__':
    main()
