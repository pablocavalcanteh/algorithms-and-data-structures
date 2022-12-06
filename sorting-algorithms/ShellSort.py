from Sorting import ISorting

class ShellSort(ISorting):
    
    def __init__(self, vector):
        super().__init__(vector)

    def sort(self) -> None:
        
        interval = len(self.vector) // 2

        while interval > 0:
            for i in range(interval, len(self.vector)):
                aux = self.vector[i]
                j = i
                while j >= interval and self.vector[j - interval] > aux:
                    self.vector[j] = self.vector[j - interval]
                    j -= interval
                self.vector[j] = aux
            interval //= 2

        return self.vector


if __name__ == "__main__":

    shellsort = ShellSort([45, 3, 2, -1, 0, 0, 1, 34])
    shellsort.sort()
    print('Ordered vector = ', shellsort.vector)
    
