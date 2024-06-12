# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1

from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Initialize the graph as an adjacency list
        graph = [[] for _ in range(n)]
        
        # Populate the adjacency list with the given edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize distances array, -1 indicates that the vertex is unreachable
        distances = [-1] * n
        
        # BFS initialization
        queue = deque([src])
        distances[src] = 0
        
        # Perform BFS
        while queue:
            node = queue.popleft()
            current_distance = distances[node]
            
            for neighbor in graph[node]:
                if distances[neighbor] == -1:  # if the neighbor has not been visited
                    distances[neighbor] = current_distance + 1
                    queue.append(neighbor)
        
        return distances

