import numpy as np
from typing import Union
from Vector import Vector

class UnorderedVector(Vector):

    def __init__(self, size):
        super().__init__(size)
    
    def print(self) -> None:

        if self.position_last == -1:
            print('Vector is empty!')
        else:
            for i in range(self.position_last + 1):
                print(f'Index {i}:', self.values[i])
    
    def insert(self, value) -> None:
        
        if self.position_last == self.size - 1:
            print('No space!')
        else:
            self.position_last += 1
            self.values[self.position_last] = value
    
    def delete(self, value) -> Union[None, int]:
        position =  self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.position_last):
                self.values[i] = self.values[i + 1]
            
            self.position_last -= 1
    
    def search(self, value) -> int:
        
        for i in range(self.position_last + 1):
            if value == self.values[i]:
                return i
        return -1

if __name__ == "__main__":

    vector = UnorderedVector(10)
    vector.print()

    for i in range(1, 11):
        vector.insert(i)

    vector.print()
    print('-------------')

    vector.delete(5)

    vector.print()

    print('-------------')
    print(f'Position last: {vector.position_last}')

