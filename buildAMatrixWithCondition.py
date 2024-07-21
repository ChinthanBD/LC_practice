# https://leetcode.com/problems/build-a-matrix-with-conditions/description/?envType=daily-question&envId=2024-07-21
from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            # Create adjacency list and indegree count
            adj_list = defaultdict(list)
            indegree = [0] * (k + 1)
            
            for u, v in conditions:
                adj_list[u].append(v)
                indegree[v] += 1
            
            # Queue for nodes with 0 indegree
            queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            sorted_order = []
            
            while queue:
                node = queue.popleft()
                sorted_order.append(node)
                
                for neighbor in adj_list[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(sorted_order) == k:
                return sorted_order
            else:
                return []
        
        # Get topological sorts for rows and columns
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        # If either sort is empty, no valid matrix can be formed
        if not row_order or not col_order:
            return []
        
        # Create position maps for row and column orders
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        # Initialize k x k matrix with 0s
        matrix = [[0] * k for _ in range(k)]
        
        # Place each number in its respective position
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix
