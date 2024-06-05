# https://www.geeksforgeeks.org/problems/topological-sort/1

from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited = set()  # Set to keep track of visited vertices
        stack = []  # Stack to store the topological sort order

        def dfs(node):
            visited.add(node)  # Mark the current node as visited
            # Recur for all the vertices adjacent to this vertex
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)  # Perform DFS on the unvisited neighbor
            stack.append(node)  # Push the current node to the stack after visiting all its neighbors

        # Perform DFS for all vertices to cover disconnected components
        for i in range(V):
            if i not in visited:
                dfs(i)  # Call DFS on the unvisited vertex

        # Return the reverse of the stack which represents the topological order
        return stack[::-1]


### BFS Solution --> Kahn's Algo 

    def topoSort(self, V, adj):
        topsort = []  # List to store the topological sort order
        indegree = {}  # Dictionary to store the in-degree of each vertex
        
        # Initialize the in-degree dictionary with all vertices having in-degree 0
        for i in range(V):
            indegree[i] = 0
            
        # Calculate the in-degree for each vertex
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1
        
        q = deque()  # Queue to manage vertices with in-degree 0
        
        # Enqueue all vertices with in-degree 0
        for node, incoming_nodes in indegree.items():
            if incoming_nodes == 0:
                q.append(node) 
        
        # Process the vertices in the queue
        while q:
            curr_node = q.popleft()  # Dequeue a vertex with in-degree 0
            topsort.append(curr_node)  # Add it to the topological sort order
            
            # Reduce the in-degree of all its neighbors
            for neighbour in adj[curr_node]:
                indegree[neighbour] -= 1
                    
                # If the in-degree of a neighbor becomes 0, enqueue it
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        return topsort  # Return the topological sort order
