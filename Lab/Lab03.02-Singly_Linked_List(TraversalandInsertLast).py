class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, count=None):
        self.count = 0
        self.head = None
    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1
    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
            return
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print("")

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()