import numpy as np

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.start = 0
        self.final = -1
        self.elements_number = 0
        self.values = np.empty(self.size, dtype=int)

    def __empty_queue(self):
        return self.elements_number == 0
    
    def __full_queue(self):
        return self.elements_number == self.size
    
    def push(self, value):

        if self.__full_queue():
            print('Queue is full!')
            return

        if  self.final == self.size -1:
            self.final = -1
        self.final += 1
        self.values[self.final] = value
        self.elements_number += 1
    
    def pop(self):

        if self.__empty_queue():
            print('Queue is empty!')
            return
        
        aux = self.values[self.start]
        self.start += 1

        if self.start == self.size:
            self.start = 0
        
        self.elements_number -= 1
        return aux
    
    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.start]

if __name__ == "__main__":

    queue = CircularQueue(10)

    queue.push(9)
    queue.push(7)
    queue.push(5)

    print(queue.first())

    queue.pop()

    print(queue.first())


