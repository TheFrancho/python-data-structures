class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


    def __str__(self):
        return f'stored data: {self.data} linked to {self.next.data if self.next != None else None} '

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B", node1)
    node3 = Node("C", node2)

    collection = [node1, node2, node3]
    
    for i in collection:
        print(i)