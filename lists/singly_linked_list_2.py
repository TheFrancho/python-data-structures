from dataclasses import dataclass
from node_2 import Node

@dataclass
class SinglyLinkedList:
    # tail : any = None
    # size : int = 0

    def __init__(self):
        self.tail = None
        self.size = 0


    def append(self,data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
            self.size+=1
        else:
            current = self.tail

            while current.next:
                current = current.next
            
            current.next = node
            self.size+=1
    

    def size(self):
        return str(self.size)

    
    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val
    

    def add(self, position, data):
        if position > self.size or position < 1:
            return False
        


    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size-=1
                    return current.data
            
            previous = current
            current = current.next
    

    def search(self,data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found')

    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
    

    def __str__(self) -> str:
        str_repr = ''
        for i in self.iter():
            str_repr +=str(i) + ","
        return str_repr[:-1]
    

if __name__ == '__main__':
    singly_list = SinglyLinkedList()
    singly_list.append(121)
    singly_list.append(232)
    singly_list.append(343)
    print(singly_list)