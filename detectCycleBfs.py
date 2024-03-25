# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph using BFS.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        
        # Set to keep track of visited nodes
        visited = set()
        
        # Function to perform BFS traversal and detect cycle
        def bfs_detect_cycle(node, parent):
            # Initialize a queue for BFS traversal, starting with the given node and its parent
            queue = deque([(node, parent)])
            while queue:
                # Dequeue a node and its parent from the queue
                node, parent = queue.popleft()
                # Mark the current node as visited
                visited.add(node)
                
                # Traverse the neighbors of the current node
                for neighbour in adj[node]:
                    # If the neighbor is not visited, enqueue it with the current node
                    if neighbour not in visited:
                        queue.append((neighbour, node))
                    # If the neighbor is visited and not the parent of the current node, a cycle is detected
                    elif neighbour != parent:
                        return True
            # If no cycle is detected in the BFS traversal, return False
            return False
                        
    
        # Iterate over all vertices in the graph
        for i in range(V):
            parent = -1  # Initialize parent as -1
            # If the current vertex is not visited, perform BFS traversal from it to detect cycle
            if i not in visited:
                if bfs_detect_cycle(i, parent):
                    return True  # If cycle detected, return True
        # If no cycle is detected after traversing all vertices, return False
        return False
