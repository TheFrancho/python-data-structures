from node_2 import Node

class Stack:
    

    def __init__(self):
        self.top = None
        self.size = 0
    

    def push(self,data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size+=1
    

    def pop(self):
        if self.top:
            data = self.top.data
            self.size-=1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
        
            return data
        
        else:
            return 'The Stack is empty'
    

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return 'The Stack is empty'
        
    
    def clear(self):
        while self.top:
            self.pop()
    

    def iter(self):
        current = self.top
        counter = 0
        while  counter < self.size:
            val = current.data
            current = current.next
            counter+=1
            yield val
    

    def __str__(self):
        str_repr = ''
        for i in self.iter():
            str_repr +=str(i) + ","
        return str_repr[:-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)