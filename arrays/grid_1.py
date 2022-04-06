from arrays.array_1 import Array
import random

class Grid:

    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)


    def get_height(self):
        return len(self.data)

    
    def get_widht(self):
        return len(self.data[0])


    def fill_matrix(self):
        for row in range(self.get_height()):
            for col in range(self.get_widht()):
                self.data[row][col] = random.randint(1,50)
    
    def __getitem__(self, index):
        return self.data[index]


    def __str__(self):
        result = ''
        for row in range(self.get_height()):
            for col in range(self.get_widht()):
                result+=str(self.data[row][col]) + ' '
            result+= '\n'
        return str(result)


if __name__ == '__main__':
    grid = Grid(rows= 5,columns= 5)
    grid.fill_matrix()
    print(grid)