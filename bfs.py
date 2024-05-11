# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
from typing import List
from collections import deque 
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        queue = deque([]) # to store the nodes to acheive bfs
        visited = set() # maintain the nodes which are already visited
        traversal = [] # list to maintain traversal
        queue.append(0)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                for neighbour in adj[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return traversal    