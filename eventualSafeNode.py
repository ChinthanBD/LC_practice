# https://www.geeksforgeeks.org/problems/eventual-safe-states/1

from typing import List

class Solution:    
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        ans = []
        visited = [False] * V
        pathVisited = [False] * V
        check = [False] * V
        
        def dfs(node):
            if pathVisited[node]:
                return True  # Cycle detected
            if visited[node]:
                return False  # Already processed and no cycle
            
            visited[node] = True
            pathVisited[node] = True
            
            for neighbour in adj[node]:
                if dfs(neighbour):
                    return True
            
            pathVisited[node] = False
            check[node] = True
            return False
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        for i in range(V):
            if check[i]:
                ans.append(i)
        
        return ans