'''Lab02.04-ParenthesesMatching'''
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
    def is_empty(self):
        return self.size == 0
def is_parentheses_matching(expression):
    stack = ArrayStack()
    is_unmatched_found = False
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            popped = stack.pop()
            if popped is None:
                is_unmatched_found = True
    if not is_unmatched_found and stack.is_empty():
        print(f'Parentheses in {expression} are matched')
        return True
    else:
        print(f'Parentheses in {expression} are unmatched')
        return False
expr = input()
result = is_parentheses_matching(expr)
print(result)
