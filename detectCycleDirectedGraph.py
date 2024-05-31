# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from collections import deque
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


############### BFS Solution using Kahn's algo ###################

    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize the in-degree dictionary with zero for each vertex
        indegree = {i: 0 for i in range(V)}
        
        # Compute in-degrees of all vertices by counting incoming edges
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1
        
        # Initialize a queue and enqueue all vertices with in-degree of 0
        q = deque([node for node, incoming_node in indegree.items() if incoming_node == 0])
        
        # Initialize the counter for the number of nodes processed
        ans = 0
        
        # Process nodes in the queue
        while q:
            curr_node = q.popleft()  # Dequeue a vertex with in-degree 0
            ans += 1  # Increment the counter
            
            # Decrease in-degree of all adjacent vertices (neighbors)
            for neighbour in adj[curr_node]:
                indegree[neighbour] -= 1
                # If in-degree becomes 0, enqueue the neighbor
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        # If the number of processed nodes is not equal to V, there is a cycle
        return ans != V
