from Sorting import ISorting

class InsertionSort(ISorting):

    def __init__(self, vector):
        super().__init__(vector)
    
    def sort(self) -> None:
        
        elements_number = len(self.vector)

        for i in range(1, elements_number):

            marked = self.vector[i]

            j = i - 1
            while j >= 0 and marked < self.vector[j]:
                self.vector[j + 1] = self.vector[j]
                j -= 1
            self.vector[j + 1] = marked

        return self.vector

if __name__ == "__main__":

    insertion = InsertionSort([45, 3, 2, -1, 0, 0, 1, 34])
    insertion.sort()
    print('Ordered vector = ', insertion.vector)
        
