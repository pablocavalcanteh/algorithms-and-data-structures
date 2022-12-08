
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