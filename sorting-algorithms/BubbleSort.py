from Sorting import ISorting

class BubbleSorting(ISorting):
    
    def __init__(self, vector):
        super().__init__(vector)

    def sort(self) -> None:
        
        elements_number = len(self.vector)

        for i in range(elements_number):
            for j in range(0, (elements_number-i-1)):
                if self.vector[j] > self.vector[j+1]:
                    aux = self.vector[j]
                    self.vector[j] = self.vector[j+1]
                    self.vector[j+1] = aux
        return self.vector


if __name__ == "__main__":

    bs = BubbleSorting([45, 3, 2, -1, 0, 0, 1, 34])
    bs.sort()
    print('Ordered vector = ', bs.vector)
    
