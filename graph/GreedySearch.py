import numpy as np

class Vertex:
    
    def __init__(self, label, goal_distance):
        self.label = label
        self.goal_distance = goal_distance
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

    arad = Vertex('Arad', 366)
    zerind = Vertex('Zerind', 374)
    oradea = Vertex('Oradea', 380)
    sibiu = Vertex('Sibiu', 253)
    timisoara = Vertex('Timisoara', 329)
    lugoj = Vertex('Lugoj', 244)
    mehadia = Vertex('Mehadia', 241)
    dobreta = Vertex('Dobreta', 242)
    craiova = Vertex('Craiova', 160)
    rimnicu = Vertex('Rimnicu', 193)
    fagaras = Vertex('Fagaras', 178)
    pitesti = Vertex('Pitesti', 98)
    bucharest = Vertex('Bucharest', 0)
    giurgiu = Vertex('Giurgiu', 77)

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

class OrderedVector:
  
  def __init__(self, size):
    self.size = size
    self.last_position = -1
    self.values = np.empty(self.size, dtype=object)

  def insert(self, vertex):
    if self.last_position == self.size - 1:
      print('Maximum capacity has been reached')
      return
    position = 0
    for i in range(self.last_position + 1):
      position = i
      if self.values[i].goal_distance > vertex.goal_distance:
        break
      if i == self.last_position:
        position = i + 1
    x = self.last_position
    while x >= position:
      self.values[x + 1] = self.values[x]
      x -= 1
    self.values[position] = vertex
    self.last_position += 1

  def print(self):
    if self.last_position == -1:
      print('The vector is empty!')
    else:
      for i in range(self.last_position + 1):
        print(i, ' - ', self.values[i].label, ' - ', self.values[i].goal_distance)

class GreedySearch:

  def __init__(self, goal):
    self.goal = goal
    self.found = False

  def search(self, current):
    print('Current: {}'.format(current.label))
    current.visited = True

    if current == self.goal:
      self.found = True
    else:
      ordered_vector = OrderedVector(len(current.adjacent))
      for adjacent in current.adjacent:
        if adjacent.vertex.visited == False:
          adjacent.vertex.visited == True
          ordered_vector.insert(adjacent.vertex)
      ordered_vector.print()

      if ordered_vector.values[0]:
        self.search(ordered_vector.values[0]) 

if __name__ == "__main__":

  graph = Graph()

  vector = OrderedVector(5)
  vector.insert(graph.arad)
  vector.insert(graph.craiova)
  vector.insert(graph.bucharest)
  vector.insert(graph.dobreta)

  greedy_search = GreedySearch(graph.bucharest)
  greedy_search.search(graph.arad)