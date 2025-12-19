'''Exercise02.01-InfixtoPostfixV.1'''
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
def infixToPostfix(expression):
    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
    stack = ArrayStack()
    postfix = ''
    for char in expression:
        if char == ' ':
            continue
        if char not in precedence:
            postfix += char
        else:
            while (not stack.is_empty() and precedence.get(stack.get_stack_top(), 0)
                >= precedence[char]):
                postfix += stack.pop()
            stack.push(char)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix
exp = input()
print(infixToPostfix(exp))
