# https://www.geeksforgeeks.org/problems/bipartite-graph/1
from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        # Initialize a color array to store colors assigned to all vertices.
        # -1 indicates no color is assigned yet.
        color = [-1] * V
        
        # A helper function to check bipartiteness from a given source node.
        def bfs_check(start):
            queue = deque([start])
            color[start] = 0  # Start coloring the source node with color 0.
            
            while queue:
                node = queue.popleft()
                
                # Check all adjacent vertices of the dequeued node.
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        # If the neighbor hasn't been colored, assign it the opposite color.
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # If the neighbor has the same color as the current node, it's not bipartite.
                        return False
            return True
        
        # Check each component of the graph.
        for i in range(V):
            if color[i] == -1:  # If the vertex is not colored, start a BFS check.
                if not bfs_check(i):
                    return False
        
        return True
    
##################################### 


class Solution:
    def isBipartite(self, V, adj):
        visited = set()
        color = {}
        def dfs(node,c):
            color[node] = c
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    if not dfs(neighbour, 1 - color[node]):
                        return False
                elif color[neighbour] == color[node]:
                        return False
            return True

        for i in range(V):
            if i not in visited:
                if not dfs(i,0):
                    return False
                
        return True
