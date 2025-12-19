'''Lab02.05-StudentGroups'''
class ArrayStack:
    def __init__(self):
        self.data = []
        self.size = 0
    def push(self, input_data):
        self.data.append(input_data)
        self.size += 1
    def pop(self):
        if self.is_empty():
            return None
        self.size -= 1
        return self.data.pop()
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
def distribute_students():
    m = int(input())
    n = int(input())
    main_stack = ArrayStack()
    for _ in range(n):
        main_stack.push(input())
    groups = []
    for _ in range(m):
        groups.append(ArrayStack())
    current_group = 0
    while not main_stack.is_empty():
        student = main_stack.pop()
        groups[current_group].push(student)
        current_group = (current_group + 1) % m
    for i in range(m):
        print(f'Group {i+1}: ',end='')
        group_stack = groups[i]
        for index in range(group_stack.get_size()):
            student_name = group_stack.data[index]
            if index == group_stack.get_size() - 1:
                print(student_name)
            else:
                print(student_name, end=", ")
distribute_students()
