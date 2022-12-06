from Sorting import ISorting

class MergeSorting(ISorting):
    
    def __init__(self, vector):
        super().__init__(vector)

    def sort(self, vector_half = None) -> None:

        if not vector_half and vector_half != None:
            return
        if vector_half is None:
            vector_half = self.vector
        
        if len(vector_half) > 1:
            half = len(vector_half) // 2
            left = vector_half[:half].copy()
            right = vector_half[half:].copy()

            self.sort(left)
            self.sort(right)

            i = j = k = 0

            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    vector_half[k] = left[i]
                    i += 1
                else:
                    vector_half[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                vector_half[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                vector_half[k] = right[j]
                j += 1
                k += 1
                
        return vector_half


if __name__ == "__main__":

    ms = MergeSorting([45, 3, 2, -1, 0, 0, 1, 34])
    ms.sort()
    print('Ordered vector = ', ms.vector)
    
