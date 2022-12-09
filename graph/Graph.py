
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


if __name__ == "__main__":

    graph = Graph()

    graph.arad.show_adjacent()