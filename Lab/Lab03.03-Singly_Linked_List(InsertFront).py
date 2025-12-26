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
    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        # elif condition == "B":
        #     mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()