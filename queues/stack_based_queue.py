class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
    

    def enqueue(self, data):
        self.inbound_stack.append(data)


    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        return self.outbound_stack.pop()

if __name__ == '__main__':
    queue = Queue()

    queue_filler = [i*10 for i in range(5,11)]

    for i in queue_filler:
        queue.enqueue(i)
    
    print(queue.inbound_stack)
    queue.enqueue(110)
    print(queue.inbound_stack)
    queue.dequeue()
    print(queue.outbound_stack)