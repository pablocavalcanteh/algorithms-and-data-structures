import numpy as np

class Deque:
    
    def __init__(self, size):
        self.size = size
        self.start = -1
        self.final = 0
        self.elements_number = 0
        self.values = np.empty(self.size, dtype=int)
    
    def __full_deque(self):
        return (self.start == 0 and self.final == self.size - 1) or (self.start == self.final + 1)
    
    def __empty_deque(self):
        return self.start == -1
    
    def insert_start(self, value):

        if self.__full_deque():
            print('Deque is full!')
            return
        
        if self.start == -1:
            self.start = 0
            self.final = 1
        elif self.start == 0:
            self.start = self.size - 1
        else:
            self.start -= 1
        
        self.values[self.start] = value

    def insert_final(self, value):

        if self.__full_deque():
            print('Deque is full!')
            return
        
        if self.start == -1:
            self.start = 0
            self.final = 0
        elif self.final == self.size - 1:
            self.final = 0
        else:
            self.final += 1
        
        self.values[self.final] = value
    
    def delete_start(self):

        if self.__empty_deque():
            print('Deque is empty!')
            return
        
        if self.start == self.final:
            self.start = -1
            self.final = -1
        elif self.start == self.size -1:
            self.start = 0
        else:
            self.start += 1
    
    def delete_final(self):

        if self.__empty_deque():
            print('Deque is empty!')
            return
        
        if self.start == self.final:
            self.start = -1
            self.final = -1
        elif self.start == 0:
            self.final = self.size -1
        else:
            self.final -= 1

    def first_element(self):
        if self.__empty_deque():
            print('Deque is empty!')
            return
        
        return self.values[self.start]

    def last_element(self):
        if  self.__empty_deque() or self.final < 0:
            print('Deque is empty!')
            return
        
        return self.values[self.final]


if __name__ == "__main__":

    deque = Deque(10)

    deque.insert_start(1)
    deque.insert_start(2)
    deque.insert_final(5)
    deque.insert_final(7)

    print(deque.first_element())
    print(deque.last_element())