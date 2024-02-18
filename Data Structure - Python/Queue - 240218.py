class Queue:
    def __init__(self):
        self.container = []
    
    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def enqueue(self, data):
        self.container.append(data)
        
    def dequeue(self):
        if self.container:
            self.container.pop(0)
        else:
            print("This Queue is empty")
    
    def peek(self):
        return self.container[0]