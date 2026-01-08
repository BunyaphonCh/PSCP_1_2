class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinked:
    def __init__(self):
        self.head = None
    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        if current is not None:
            new_node.next = current.next
            current.next = new_node
    def print_lis(self):
        current = self.head
        first = True
        while current is not None:
            if not first:
                print(' ', end='')
            print(current.data, end='')
            first = False
            current = current.next
def main():
    try:
        line = input()
        if not line:
            return
        n = int(line)
        sl = SinglyLinked()
        for _ in range(n):
            data_line = input()
            sl.push_back(int(data_line))
        index_line = input()
        idx = int(index_line)
        val_line = input()
        val = int(val_line)
        sl.insert_at_index(idx, val)
        sl.print_lis()
    except ValueError:
        pass
if __name__ == '__main__':
    main()
