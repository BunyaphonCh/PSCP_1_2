class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1
        
class ResultLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def traverse(self):
        current = self.head
        if current is None:
            return
        print(current.data, end='')
        current = current.next
        while current is not None:
            print(' -> ' +str(current.data), end='')
            current = current.next
        print()
def main():
    try:
        line = input()
        n = int(line)
    except:
        return
    source = DoublyLinkedList()
    for i in range(n):
        try:
            val = input()
            source.add_node(val)
        except:
            break
    if source.count == 0:
        return
    result = ResultLinkedList()
    left = source.head
    right = source.tail
    processed = 0
    total = source.count
    if processed < total:
        result.add_node(right.data)
        right = right.prev
        processed += 1
    while processed < total:
        for i in range(2):
            if processed < total:
                result.add_node(left.data)
                left = left.next
                processed += 1
        for i in range(2):
            if processed < total:
                result.add_node(right.data)
                right = right.prev
                processed += 1
    result.traverse()
if __name__ == '__main__':
    main()
