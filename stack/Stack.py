import numpy as np

class Stack:

    def __init__(self, size):
        self.__size = size
        self.__top = -1
        self.__values = np.empty(self.__size, dtype=int)
    
    def __full_stack(self) -> bool:

        if self.__top == self.__size -1:
            return True
        else:
            return False
    
    def __empty_stack(self) -> bool:
        
        if self.__top == -1:
            return True
        else:
            return False
    
    def push(self, value) -> None:

        if self.__full_stack():
            print('Stack is full!')
        else:
            self.__top += 1
            self.__values[self.__top] = value
    

    def pop(self) -> None:

        if self.__empty_stack():
            print('Stack is empty!')
        else:
            self.__top -= 1
    

    def show_top(self) -> int:

        if self.__top != -1:
            return self.__values[self.__top]
        else:
            return -1

if __name__ == "__main__":

    stack = Stack(10)

    stack.push(1)
    stack.push(3)
    stack.push(5)

    print(stack.show_top())

    stack.pop()
    print(stack.show_top())

    stack.pop()
    print(stack.show_top())


