# https://bit.ly/3yR3dIB
class Solution:
    def numProvinces(self, adj, V):
        # Depth-First Search (DFS) function to traverse the graph
        def dfs(node):
            # Mark the current node as visited
            if not visited[node]:
                visited[node] = True
                # Iterate over the neighbors of the current node
                for neighbour in range(V):
                    # If there is a connection to the neighbour and it's not visited yet
                    if adj[node][neighbour] and not visited[neighbour]:
                        # Recursively explore the neighbour
                        dfs(neighbour)
        
        # Initialize a list to keep track of visited nodes
        visited = [False] * V
        # Initialize a variable to count the number of provinces
        province_count = 0
        
        # Iterate over each node in the graph
        for node in range(V):
            # If the node has not been visited yet, start DFS from that node
            if not visited[node]:
                dfs(node)
                # Increment the province count after exploring all nodes in the connected component
                province_count += 1
        
        # Return the total count of provinces
        return province_count

