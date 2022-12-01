
from typing import Union


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
    def print(self) -> None:
        print(self.value)

class LinkedListDoubly:

    def __init__(self):
        self.first = None
        self.last = None
    
    def __empty_list(self) -> bool:
        return self.first == None
    
    def insert_start(self, value) -> None:
        new_node = Node(value)
        if self.__empty_list():
            self.last = new_node
        else:
            self.first.previous = new_node
        new_node.next = self.first
        self.first = new_node
    
    def insert_final(self, value) -> None:
        new_node = Node(value)
        if self.__empty_list():
            self.first= new_node
        else:
            self.last.next = new_node
            new_node.previous = self.last
        self.last = new_node
    
    def delete_start(self) -> Union[None, int]:
        aux = self.first
        if not self.first.next:
            self.last = None
        else:
            self.first.next.previous = None
        self.first = self.first.next
        return aux
    
    def delete_final(self) -> Union[None, Node]:
        aux = self.last
        if not self.first.next:
            self.first = None
        else:
            self.last.previous.next = None
        self.last = self.last.previous
        return aux
    
    def delete_position(self, value) -> Union[None, Node]:
        current = self.first
        while current.value != value:
            current = current.next
            if not current:
                return None
        if current == self.first:
            self.first == current.next
        else:
            current.previous.next = current.next
        
        if current == self.last:
            self.last = current.previous
        else:
            current.next.previous = current.previous
        return current
    
    def print_first(self) -> None:
        current = self.first
        while current:
            current.print()
            current = current.next
    
    def print_last(self) -> None:
        current = self.last
        while current:
            current.print()
            current = current.previous

if __name__ == "__main__":

    list = LinkedListDoubly()

    list.insert_start(1)
    list.insert_start(2)
    list.insert_start(3)
    list.insert_final(4)

    list.print_first()
    print('---------------------------')

    list.print_last()
