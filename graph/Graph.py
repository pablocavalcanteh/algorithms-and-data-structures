from typing import Union
import numpy as np

class Stack:

    def __init__(self, size):
        self.__size = size
        self.__top = -1
        self.__values = np.empty(self.__size, dtype=Vertex)
    
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
    

    def pop(self) -> object:

        if self.__empty_stack():
            print('Stack is empty!')
            return None
        else:
            vtx = self.__values[self.__top]
            self.__top -= 1
            return vtx
    

    def show_top(self) -> int:

        if self.__top != -1:
            return self.__values[self.__top]
        else:
            return -1

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.start = 0
        self.final = -1
        self.elements_number = 0
        self.values = np.empty(self.size, dtype=Vertex)
    
    def empty_queue(self) -> bool:
        return self.elements_number == 0
    
    def full_queue(self) -> bool:
        return self.elements_number == self.size
    
    def push(self, value):

        if self.full_queue():
            print('Queue is full!')
            return

        if  self.final == self.size -1:
            self.final = -1
        self.final += 1
        self.values[self.final] = value
        self.elements_number += 1
    
    def pop(self):

        if self.empty_queue():
            print('Queue is empty!')
            return
        
        aux = self.values[self.start]
        self.start += 1

        if self.start == self.size:
            self.start = 0
        
        self.elements_number -= 1
        return aux
    
    def first(self):
        if self.empty_queue():
            return -1
        return self.values[self.start]

class Vertex:
    
    def __init__(self, label):
        self.label = label
        self.visited =  False
        self.adjacent = []
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for obj in self.adjacent:
            print(obj.vertex.label, obj.cost)

class Adjacent:

    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

class Graph:

    def __init__(self):
        pass

    arad = Vertex('Arad')
    zerind = Vertex('Zerind')
    oradea = Vertex('Oradea')
    sibiu = Vertex('Sibiu')
    timisoara = Vertex('Timisoara')
    lugoj = Vertex('Lugoj')
    mehadia = Vertex('Mehadia')
    dobreta = Vertex('Dobreta')
    craiova = Vertex('Craiova')
    rimnicu = Vertex('Rimnicu')
    fagaras = Vertex('Fagaras')
    pitesti = Vertex('Pitesti')
    bucharest = Vertex('Bucharest')
    giurgiu = Vertex('Giurgiu')

    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))

class DepthFirstSearch:

    def __init__(self, initial):
        self.initial = initial
        self.initial.visited = True
        self.stack = Stack(20)
        self.stack.push(initial)
    
    def search(self) -> None:
        top = self.stack.show_top()
        print('Top: {}'.format(top.label))
        for adjacent in top.adjacent:
            print('Top is {}. {} Have already been  visited? {}'.format(top.label, adjacent.vertex.label, adjacent.vertex.visited))
            if adjacent.vertex.visited == False:
                adjacent.vertex.visited = True
                self.stack.push(adjacent.vertex)
                print('Push: {}'.format(adjacent.vertex.label))
                self.search()
        print('Pop: {}'.format(self.stack.pop().label))
        print()

class BreadthFirstSearch:

    def __init__(self, initial):
        self.initial = initial
        self.initial.visited = True
        self.queue = CircularQueue(20)
        self.queue.push(initial)

    def search(self):
        first = self.queue.first()
        print('First of queue: {}'.format(first.label))
        aux = self.queue.pop()
        print('Pop: {}'.format(aux.label))
        for adjacent in first.adjacent:
            print('Fisrt was {}. {} Have already been visited? {}'.format(aux.label, adjacent.vertex.label, adjacent.vertex.visited))
            if adjacent.vertex.visited == False:
                adjacent.vertex.visited = True
                self.queue.push(adjacent.vertex)
                print('Push: {}'.format(adjacent.vertex.label))
        if self.queue.elements_number > 0:
            self.search()

if __name__ == "__main__":

    graph = Graph()

    graph.arad.show_adjacent()

    dfs = DepthFirstSearch(graph.arad)
    dfs.search()

    print('-----------------------')
    bfs = BreadthFirstSearch(graph.arad)
    bfs.search()