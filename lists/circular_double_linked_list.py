from dataclasses import dataclass
from node_2 import Node, TwoWayNode

#@dataclass
class CircularDoubleLinkedList:


    def __init__(self):
        self.tail = None
        self.size = 0


    def append(self,data):
        node = TwoWayNode(data)
        counter = 1
        piv = None
        if self.tail == None:
            self.tail = node
            self.tail.next = self.tail
            self.tail.previous = self.tail
            self.size+=1
        else:
            current = self.tail
            while counter < self.size:
                current = current.next
                counter+=1
            
            current.next = node
            current.next.next = self.tail
            current.next.previous = current
            self.size+=1
    

    def size(self):
        return str(self.size)

    
    def iter(self):
        current = self.tail
        counter = 0
        while current and counter < self.size:
            val = current.data
            current = current.next
            counter+=1
            yield val
    

    def add(self, position, data):
        node = Node(data)
        current = self.tail

        if position > self.size or position < 1:
            print("error, lol")
            return False
            
        counter = 2

        if position == 1:
            self.tail = node
            node.next = current
            self.size+=1
        else:
            while counter < position:
                current = current.next
                counter +=1
            node.next = current.next
            node.previous = current
            current.next = node
            self.size+=1
            

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.tail.previous = current.next
                else:
                    previous.next = current.next
                    current.next.previous = previous
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
        self.size = 0
    

    def __str__(self):
        str_repr = ''
        for i in self.iter():
            str_repr +=str(i) + ","
        return str_repr[:-1]
    

    def show_connections(self):
        current = self.tail
        counter = 0
        while counter < self.size:
            val = current.data
            print(f'Value {val} connected to {current.previous.data} and {current.next.data}')
            current = current.next
            counter+=1

if __name__ == '__main__':
    singly_list = CircularDoubleLinkedList()
    fill_singly_list = [i*121 for i  in range(1,6)]

    for i in fill_singly_list:
        singly_list.append(i)

    print('current list: ' + str(singly_list))

    singly_list.add(5, -121)
    print('adding -121 to position 5: ' + str(singly_list))

    # singly_list.delete(-121)
    # print('deleting the element -121: ' + str(singly_list))

    singly_list.show_connections()