# # https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph using BFS.


    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()  # Set to store visited nodes
        
        def dfs_detect_cycle(node, parent):
            visited.add(node)  # Mark current node as visited
            for neighbour in adj[node]:  # Iterate over neighbours of the current node
                if neighbour not in visited:  # If neighbour is not visited yet
                    if dfs_detect_cycle(neighbour, node):  # Recursively traverse the neighbour
                        return True
                elif neighbour != parent:  # If neighbour is visited and not parent, cycle detected
                    return True
            return False
        
        for i in range(V):  # Iterate over all vertices
            if i not in visited:  # If vertex is not visited yet
                if dfs_detect_cycle(i, -1):  # Perform DFS traversal from current vertex
                    return True  # If cycle detected, return True
        return False  # If no cycle detected, return False