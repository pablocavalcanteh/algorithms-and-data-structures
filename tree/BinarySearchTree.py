
from typing import Union


class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def show(self) -> None:
        print(self.value)

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.links = []
    
    def insert(self, value) -> None:

        node = Node(value)

        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                parent_node = current
                
                if value < current.value:
                    current = current.left
                    if not current:
                        parent_node.left = node
                        self.links.append(str(parent_node.value) + '->' + str(node.value))
                        return
                else:
                    current = current.right
                    if not current:
                        parent_node.right = node
                        self.links.append(str(parent_node.value) + '->' + str(node.value))
                        return
    
    def search(self, value) -> Union[Node, None]:
        current_node = self.root
        while current_node.value != value:
            if value < current_node.value:
                current_node = current_node.value
            else:
                current_node = current_node.right
            if not current_node:
                return None
        return current_node
    
    # Root, lelf and right
    def pre_order(self, node: Node) -> None:

        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    # Left, root, right
    def in_order(self, node: Node) -> None:
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)
    
    def pos_order(self, node: Node) -> None:
        if node:
            self.pos_order(node.left)
            self.pos_order(node.right)
            print(node.value)
    
    
