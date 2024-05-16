# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = set() # maintain visisted nodes 
        traversal = []
        def dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                for neighbour in adj[vertex]:
                    if neighbour not in visited:
                        dfs(neighbour)
        dfs(0)
            
        return traversal