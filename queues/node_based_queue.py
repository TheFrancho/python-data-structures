class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class TwoWayNode(Node):
    def __init__(self, data, previous = None, next=None):
        super().__init__(data, next)
        self.previous = previous

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    

    def enqueue(self, data):
        node = TwoWayNode(data,None,None)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        
        self.count +=1
    
    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -=1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -=1
        
        return current.data