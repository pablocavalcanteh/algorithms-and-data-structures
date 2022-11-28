import numpy as np

class Queue:

    def __init__(self, size):
        self.size = size
        self.start = 0
        self.final = -1
        self.elements_number = 0
        self.values = np.empty(self.size, dtype=int)
    
    def empty_queue(self) -> bool:
        return self.elements_number == 0
    
    def full_queue(self) -> bool:
        return self.elements_number == self.size