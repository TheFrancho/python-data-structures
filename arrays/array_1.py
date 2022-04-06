import random

'''Class for custom data-structure array'''

class Array:

    '''Constructor method for Array class
    Recive capacity to set the array limit'''
    def __init__(self, capacity: int, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    '''Returns the array lenght'''
    def __len__(self):
        return len(self.items)
    
    '''Returns the string representation of the array'''
    def __str__(self):
        return str(self.items)

    '''Returns the iteration of the data-structure'''
    def __iter__(self):
        return iter(self.items)

    '''Get an item of the array depending of the index'''
    def __getitem__(self, index):
        return self.items[index]

    '''Set a new value on the array depending of the index'''  
    def __setitem__(self, index, new_value):
        self.items[index] = new_value

    
    def __fillitems__(self):
        self.items = [random.randint(1,10) for i in self.items]
    

    def __sumitems__(self):
        counter = 0
        for i in range(self.items):
            counter+=self.items[i]


if __name__ == '__main__':
    array = Array(5)
    print(f'Initial array: {array.__str__()}')
    array.__fillitems__()
    print(f'Filled array: {array.__str__()}')