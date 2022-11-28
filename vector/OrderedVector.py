import numpy as np
from typing import Union
import random

from Vector import Vector

class OrderedVector(Vector):

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
        
        # Just to figure out which index to put the new element in. 
        new_element_position = 0
        for i in range(self.position_last + 1):
            new_element_position = i
            if self.values[i] > value:
                break
            if i == self.position_last:
                new_element_position = i + 1
        
        # Shift the array elements to put the new element in.
        aux = self.position_last
        while aux >= new_element_position:
            self.values[aux + 1] = self.values[aux]
            aux -= 1
        

        self.values[new_element_position] = value
        self.position_last += 1
    
    def delete(self, value) -> Union[None, int]:
        position =  self.linear_search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.position_last):
                self.values[i] = self.values[i + 1]
            
            self.position_last -= 1
    
    def linear_search(self, value) -> int:
        
        for i in range(self.position_last + 1):
            if (value == self.values[i]) or (i == self.position_last):
                return -1
            if value == self.values[i]:
                return i

    def binary_search(self, value) -> int:
        
        inferior_limit = 0
        superior_limit = self.position_last

        while True:

            current_position = int((inferior_limit + superior_limit) / 2)

            if self.values[current_position] == value:
                return current_position
            elif inferior_limit > superior_limit:
                return -1
            elif self.values[current_position] == value:
                inferior_limit = current_position + 1
            else:
                superior_limit = current_position - 1




if __name__ == "__main__":

    vector = OrderedVector(10)
    vector.print()

    for i in range(1, 11):
        vector.insert(random.randint(1,10))

    vector.print()
    print('-------------')

    vector.delete(5)

    vector.print()

    print('-------------')
    print(f'Position last: {vector.position_last}')

