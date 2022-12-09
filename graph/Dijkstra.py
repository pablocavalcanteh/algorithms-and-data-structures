import numpy as np
import sys

class Dijkstra:

  def __init__(self, vertices, edges, initial):
    self.size = len(vertices)
    self.vertices = vertices
    self.graph = edges
    self.initial = initial

  def show_solution(self, distances):
    print('Smallest distances from {} until all others'.format(self.vertices[self.initial]))
    for vertex in range(self.size):
      print(self.vertices[vertex], distances[vertex])  

  def minimum_distance(self, distance, visited):
    minimum = sys.maxsize
    minimum_index = None
    for vertex in range(self.size):
        if distance[vertex] < minimum and visited[vertex] == False:
            minimum = distance[vertex]
            minimum_index = vertex
    return minimum_index

  def dijkstra(self):
    distance = [sys.maxsize] * self.size
    distance[self.initial] = 0
    visited = [False] * self.size

    for _ in range(self.size):
        minimum_index = self.minimum_distance(distance, visited)
        visited[minimum_index] = True
        for vertex in range(self.size):
            if self.graph[minimum_index][vertex] > 0 and visited[vertex] == False \
                and distance[vertex] > distance[minimum_index] + self.graph[minimum_index][vertex]:
                distance[vertex] = distance[minimum_index] + self.graph[minimum_index][vertex]

    self.show_solution(distance)

if __name__ == "__main__":

    vertices = {'arad': 0, 'zerind': 1, 'oradea': 2, 'sibiu': 3, 'timisoara': 4,
            'lugoj': 5, 'mehadia': 6, 'dobreta': 7, 'craiova': 8, 'rimnicu': 9,
            'fagaras': 10, 'pitesti': 11, 'bucharest': 12, 'giurgiu': 13}

    cities = {0: 'arad', 1: 'zerind', 2: 'oradea', 3: 'sibiu', 4: 'timisoara',
           5: 'lugoj', 6: 'mehadia', 7: 'dobreta', 8: 'craiova', 9: 'rimnicu',
           10: 'fagaras', 11: 'pitesti', 12: 'bucharest', 13: 'giurgiu'}

    edges = np.zeros([len(cities), len(cities)], dtype=int)


    dijkstra = Dijkstra(cities, edges, vertices['arad'])
    dijkstra.dijkstra()