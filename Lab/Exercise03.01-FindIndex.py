class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
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
    def print_node_at(self, index):
        current = self.head
        count = 1
        
        while current is not None:
            if count == index:
                print(current.data)
                return

            count += 1
            current = current.next
        print("Error")
def main():
    my_list = SinglyLinkedList()
    while True:
        text = input()
        if text == "Last":
            break
        my_list.insert_last(text)
    position = int(input())
    my_list.print_node_at(position)
main()
