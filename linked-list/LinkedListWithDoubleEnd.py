
from typing import Union


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    
    def print(self) -> None:
        print(self.value)

class LinkedListWithDoubleEnd:

    def __init__(self):
        self.first = None
        self.last = None
    
    def __empty_list(self) -> bool:
        return self.first == None
    
    def insert_start(self, value) -> None:
        new_no = Node(value)
        if self.__empty_list():
            self.last = new_no
        new_no.next = self.first
        self.first = new_no
    
    def insert_final(self, value) -> None:
        new_no = Node(value)
        if self.__empty_list():
            self.first = new_no
        else:
            self.last.next = new_no
        self.last = new_no
    
    def print(self) -> None:
        if not self.first:
            print('Linked list is empty!')
            return
        
        current_no = self.first
        while current_no:
            current_no.print()
            current_no = current_no.next
    
    def delete_start(self) -> Union[None, int]:
        if self.__empty_list():
            print('List is empty!')
            return
        
        aux = self.first
        if self.first.next == None:
            self.last = None
        self.first = self.first.next
        return aux
    
    def print(self) -> None:
        if self.__empty_list():
            print('List is empty!')
            return
        current = self.first
        while current != None:
            current.print()
            current = current.next

if __name__ == "__main__":

    list = LinkedListWithDoubleEnd()

    list.insert_start(1)
    list.insert_start(2)
    list.insert_start(3)
    list.insert_final(4)

    list.print()
    print('---------------------------')

    list.delete_start()
    list.print()
