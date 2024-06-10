# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
from collections import defaultdict
from typing import List

class Solution:
    
    def __init__(self):
        self.topo_sort = []  # Renamed to avoid conflict with method
        self.visited = set()
        self.adj = defaultdict(list)        
        
    def topo(self, node):
        self.visited.add(node)
        for neighbour, weight in self.adj[node]:
            if neighbour not in self.visited:
                self.topo(neighbour)
        self.topo_sort.append(node)

        
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:

        # Build the graph
        for u, v, weight in edges:
            self.adj[u].append((v, weight))
        
        # Perform topological sort
        for node in range(n):
            if node not in self.visited:
                self.topo(node)
        
        # Reverse topological sort order
        self.topo_sort = self.topo_sort[::-1]
        
        # Initialize distances
        distance = [float("inf")] * n
        distance[0] = 0
        
        # Process nodes in topological order
        for node in self.topo_sort:
            if distance[node] != float("inf"):
                for v, wt in self.adj[node]:
                    if distance[node] + wt < distance[v]:
                        distance[v] = distance[node] + wt
        
        # Replace unreachable distances with -1
        distance = [d if d != float("inf") else -1 for d in distance]
        
        return distance
