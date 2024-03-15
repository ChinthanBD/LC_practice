# https://leetcode.com/problems/redundant-connection/description/
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) +1)
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u,v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u,v]
            
            if root_u<root_v:
                parent[root_u] = root_v
            
            elif root_u>root_v:
                parent[root_v] = root_u

            else:
                parent[root_v] = root_u  
                rank[u] += 1
            return None
            
        for u,v in edges:
            ans = union(u,v)
            if ans:
                return ans

