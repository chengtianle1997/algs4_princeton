# Stack implement
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)