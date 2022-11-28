from Queue import Queue

class PriorityQueue(Queue):

    def __init__(self, size):
        super().__init__(size)


    def push(self, value):

        if self.full_queue():
            print('Queue is full!')
            return
        
        if self.elements_number == 0:
            self.values[self.elements_number] = value
            self.elements_number += 1
        else:
            aux = self.elements_number - 1
            while aux >= 0:
                if value > self.values[aux]:
                    self.values[aux + 1] = self.values[aux]
                else:
                     break
                aux -= 1
            self.values[aux + 1] = value
            self.elements_number += 1
    
    def pop(self):

        if self.empty_queue():
            print('Queue is empty!')
            return
        
        value = self.values[self.elements_number - 1]
        self.elements_number -= 1
        return value
    
    def first(self):
        if self.empty_queue():
            return -1
        return self.values[self.elements_number -1]

if __name__ == "__main__":

    queue = PriorityQueue(10)

    queue.push(9)
    queue.push(7)
    queue.push(5)

    print(queue.first())

    queue.pop()

    print(queue.first())


