# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
from typing import List

class Solution:
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Set to keep track of all visited nodes.
        visited = set()
        # Set to keep track of nodes in the current path of the DFS.
        pathVisited = set()

        # Helper function to perform DFS.
        def dfs(node):
            # Mark the current node as visited.
            visited.add(node)
            # Add the current node to the path visited set.
            pathVisited.add(node)
            
            # Traverse all the neighbors of the current node.
            for neighbour in adj[node]:
                # If the neighbor has not been visited, perform DFS on it.
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                # If the neighbor is in the current path, a cycle is detected.
                elif neighbour in pathVisited:
                    return True
            
            # Remove the node from the current path as we backtrack.
            pathVisited.remove(node)
            return False

        # Perform DFS for each node to cover disconnected components.
        for i in range(V):
            # If the node has not been visited, start DFS from it.
            if i not in visited:
                if dfs(i):
                    return True
        return False
