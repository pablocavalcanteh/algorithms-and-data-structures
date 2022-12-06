from Sorting import ISorting
from typing import Union, List

class QuickSort(ISorting):
    
    def __init__(self, vector):
        super().__init__(vector)

    def partition(self, param_vector, initial, final) -> int:
        pivot = param_vector[final]
        i = initial - 1

        for j in range(initial, final):
            if param_vector[j] <= pivot:
                i += 1
                param_vector[i], param_vector[j] = param_vector[j], param_vector[i]
        param_vector[i + 1], param_vector[final] = param_vector[final], param_vector[i + 1]
        return i + 1

    def sort(self, initial, final, param_vector = None) -> Union[None, List]:

        if not param_vector and param_vector != None:
            return
        if param_vector is None:
            param_vector = self.vector

        if initial < final:
            position = self.partition(param_vector, initial, final)
            self.sort(initial, position - 1, param_vector)
            self.sort(position + 1, final, param_vector)
        return param_vector

if __name__ == "__main__":

    qs = QuickSort([45, 3, 2, -1, 0, 0, 1, 34])
    qs.sort(initial=0, final=7)
    print('Ordered vector = ', qs.vector)
    
