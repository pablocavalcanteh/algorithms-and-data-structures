
from typing import Union


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    
    def print(self) -> None:
        print(self.value)

class LinkedList:

    def __init__(self):
        self.first = None
    
    def insert_start(self, value) -> None:
        new_no = Node(value)
        new_no.next = self.first
        self.first = new_no
    
    def print(self) -> None:
        if not self.first:
            print('Linked list is empty!')
            return
        
        current_no = self.first
        while current_no:
            current_no.print()
            current_no = current_no.next
    
    def search(self, value) -> Union[None, int]:
        if not self.first:
            print('Linked list is empty!')
            return
        
        current_no = self.first
        while current_no.value != value:
            if not current_no.next:
                return
            else:
                current_no = current_no.next
        
        return current_no
    
    def delete_start(self) -> Union[None, int]:
        if not self.first:
            print('Linked list is empty!')
            return

        aux = self.first
        self.first = self.first.next
        return aux
    
    def delete(self, value) -> Union[None, int]:
        if not self.first:
            print('Linked list is empty!')
            return
        
        current_no = self.first
        previous_no = self.first
        while current_no != value:
            if not current_no.next:
                return
            else:
                previous_no = current_no
                current_no = current_no.next
        
        if current_no == self.first:
            self.first = self.first.next
        else:
            previous_no.next = current_no.next

        return current_no

if __name__ == "__main__":

    list = LinkedList()

    list.insert_start(1)
    list.insert_start(2)
    list.insert_start(3)

    list.print()
    print('---------------------------')

    list.delete_start()
    list.print()

    print('Value found = ', list.search(2).value)