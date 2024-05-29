# https://www.geeksforgeeks.org/problems/topological-sort/1
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        visited = set()
        stack = []
        def dfs(node):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            
            stack.append(node)
        
        for i in range(V):
            if i not in visited:
                dfs(i)
        
        return stack[::-1]