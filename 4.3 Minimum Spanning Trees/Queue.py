# Queue implement
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)