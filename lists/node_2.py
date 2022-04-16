class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


    def __str__(self):
        return f'stored data: {self.data} linked to {self.next.data if self.next != None else None} '


class TwoWayNode(Node):
    def __init__(self, data, previous = None, next=None):
        super().__init__(data, next)
        self.previous = previous


def node_manual_usage():
    node1 = Node("A")
    node2 = Node("B", node1)
    node3 = Node("C", node2)

    collection = [node1, node2, node3]
    
    for i in collection:
        print(i)


def node_iterative_usage():
    collection = []
    head = None
    for count in reversed(range(5,11)):
        head = Node(count, head)
        collection.append(head)
    
    for i in reversed(collection):
        print(i)


if __name__ == '__main__':
    node_iterative_usage()
    