'''Exercise02.03-SPÄM'''
class ArrayStack:
    def __init__(self):
        self.data = []
        self.size = 0
    def push(self, input_data):
        self.data.append(input_data)
        self.size += 1
    def pop(self):
        if self.is_empty():
            print('Underflow: Cannot pop data from an empty list')
            return None
        self.size -= 1
        return self.data.pop()
    def get_stack_top(self):
        if self.is_empty():
            return None
        return self.data[-1]
    def is_empty(self):
        return self.size == 0
def is_parentheses_matching(label):
    stack = ArrayStack()
    matching_dict = {']' : '[', '}' : '{', ')' : '('}
    is_valid = True
    for char in label:
        if char in '[{(':
            stack.push(char)
        elif char in ']})':
            target = matching_dict[char]
            while not stack.is_empty() and stack.get_stack_top() != target:
                stack.pop()
                is_valid = False
            if stack.pop() is None:
                is_valid = False
    if not stack.is_empty():
        is_valid = False
    return is_valid
label_input = input()
print(is_parentheses_matching(label_input))
