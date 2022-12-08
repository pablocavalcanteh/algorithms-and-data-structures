
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
                current_node = current_node.left
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
    
    # Left, right, root
    def pos_order(self, node: Node) -> Union[None, bool]:
        if node:
            self.pos_order(node.left)
            self.pos_order(node.right)
            print(node.value)

    def delete(self, value) -> None:
        if not self.root:
            print('The tree is empty...')
            return None
        
        current_node = self.root
        parent_node = self.root
        _left = True

        while current_node.value != value:
            parent_node = current_node

            if value < current_node.value:
                _left = True
                current_node = current_node.left
            else:
                _left = False
                current_node = current_node.right
            if not current_node:
                return False
        
        if not current_node.left and not current_node.right:
            if current_node == self.root:
                self.root = None
            elif _left:
                self.links.remove(str(parent_node.value) + '->' + str(current_node.value))
                parent_node.left = None
            else:
                self.links.remove(str(parent_node.value) + '->' + str(current_node.value))
                parent_node.right = None
        elif not current_node.right:
            self.links.remove(str(parent_node.value) + '->' + str(current_node.value))
            self.links.remove(str(current_node.value) + '->' + str(current_node.left.value))

            if current_node == self.root:
                self.root = current_node.left
                self.links.append(str(self.root.value) + '->' + str(current_node.left.value))
            
            elif _left:
                parent_node.left = current_node.left
                self.links.append(str(parent_node.value) + '->' + str(current_node.left.value))
            else:
                parent_node.right = current_node.left
                self.links.append(str(parent_node.value) + '->' + str(current_node.left.value))
        
        elif not current_node.left:

            self.links.remove(str(parent_node.value) + '->' + str(current_node.value))
            self.links.remove(str(current_node.value) + '->' + str(current_node.right.value))

            if current_node == self.root:

                self.links.append(str(self.root.value) + '->' + str(current_node.right.value))
                self.root = current_node.right

            elif _left:

                self.links.append(str(parent_node.value) + '->' + str(current_node.right.value))
                parent_node.left = current_node.right

            else:

                self.links.append(str(parent_node.value) + '->' + str(current_node.right.value))
                parent_node.right = current_node.right
        else:

            next = self.get_next(current_node)

            self.links.remove(str(parent_node.value) + '->' + str(current_node.value))
            self.links.remove(str(current_node.right.value) + '->' + str(next.value))
            self.links.remove(str(current_node.value) + '->' + str(current_node.left.value))
            self.links.remove(str(current_node.value) + '->' + str(current_node.right.value))

            if current_node == self.root:

                self.links.append(str(self.root.value) + '->' + str(next.value))     
                self.root = next

            elif _left:

                self.links.append(str(parent_node.value) + '->' + str(next.value))

                parent_node.left = next

            else:

                self.links.append(str(parent_node.value) + '->' + str(next.value))
                parent_node.right = next
            
            self.links.append(str(next.value) + '->' + str(current_node.left.value))
            self.links.append(str(next.value) + '->' + str(current_node.right.value))
            
            next.left = current_node.left

        return True
        
    def get_next(self, node: Node):
        next_parent = node
        next = node
        current = node.right
        while current != None:
            next_parent = next
            next = current
            current = current.left
        if next != node.right:
            next_parent.left = next.right
            next.right = node.right
        return next


if __name__ == "__main__":

    tree = BinarySearchTree()
    tree.insert(53)
    tree.insert(30)
    tree.insert(14)
    tree.insert(39)
    tree.insert(9)
    tree.insert(23)
    tree.insert(34)
    tree.insert(49)
    tree.insert(72)
    tree.insert(61)
    tree.insert(84)
    tree.insert(79)

    tree.pre_order(tree.root)
    print('----------------')
    tree.in_order(tree.root)
    print('----------------')
    tree.pos_order(tree.root)

    print('----------------')

    if tree.search(79):
        print('Found value!')
    else:
        print('Not found value!')
