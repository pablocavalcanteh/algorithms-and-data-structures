import numpy as np

class Vector:

    def __init__(self, size):

        self.size = size
        self.position_last = -1
        self.values = np.empty(self.size, dtype=int)
    
    def print(self) -> None:

        if self.position_last == -1:
            print('Vector is empty!')
        else:
            for i in range(self.position_last + 1):
                print(f'Index {i}:', self.values[i])