class Node:
    __slots__ = 'dest', 'next'
    def __init__(self, dest):
        self.dest = dest
        self.next = None
class BusChain:
    def __init__(self, capacity):
        self.head = None
        self.count = 0
        self.capacity = capacity
        self.dropped_passengers = 0
    def add(self, destination):
        new_node = Node(destination)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
    def unload(self, current_stop):
        if self.count == 0:
            return
        while self.head is not None and self.head.dest == current_stop:
            self.head = self.head.next
            self.dropped_passengers += 1
            self.count -= 1
        if self.head is None:
            return
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.dest == current_stop:
                prev.next = curr.next
                self.dropped_passengers += 1
                self.count -= 1
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
    def is_full(self):
        return self.count >= self.capacity
def main():
    try:
        line1 = input()
        while not line.strip(): line = input()
        p = int(line)
        line = input()
        while not line.strip(): line = input()
        n = int(line)
        bus = BusChain(p)
        for _ in range(n):
            line = input()
            parts = map(int, line.split())
            try:
                current_stop_id = next(parts)
            except StopIteration:
                continue
            bus.unload(current_stop_id)
            for val in parts:
                if bus.is_full():
                    break
                if val > current_stop_id:
                    bus.add(val)
        print(bus.dropped_passengers)
    except ValueError:
        pass
if __name__ == '__main__':
    main()
