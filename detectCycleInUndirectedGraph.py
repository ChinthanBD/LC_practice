# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Set to keep track of visited nodes
        visited = set()
        
        def bfs(node):
            q = deque()
            q.append((node, -1))  # Append node with its parent (-1 for the start node)
            visited.add(node)
            
            while q:
                curr_node, parent = q.popleft()
                
                for neighbour in adj[curr_node]:
                    if neighbour in visited:
                        if neighbour != parent:
                            return True
                    else:
                        visited.add(neighbour)
                        q.append((neighbour, curr_node))
                        
            return False
        
        # Iterate over all vertices to handle disconnected graphs
        for i in range(V):
            if i not in visited:
                if bfs(i):
                    return True
                
        return False


	#####################
    #######  dfs implementation
	    
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Set to keep track of visited nodes
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            
            for neighbour in adj[node]:
                if neighbour not in visited:
                    if dfs(neighbour, node):
                        return True
                elif neighbour != parent:
                    return True
                    
            return False

        # Iterate over all vertices to handle disconnected graphs
        for i in range(V):
            if i not in visited:
                if dfs(i, -1):
                    return True
                
        return False
	        