# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2024-07-27
from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize cost matrix with infinity
        inf = float('inf')
        cost_matrix = [[inf] * 26 for _ in range(26)]
        
        # Cost of transforming a character to itself is 0
        for i in range(26):
            cost_matrix[i][i] = 0
        
        # Update cost matrix with given transformations
        for i in range(len(original)):
            orig_idx = ord(original[i]) - ord('a')
            chng_idx = ord(changed[i]) - ord('a')
            cost_matrix[orig_idx][chng_idx] = min(cost_matrix[orig_idx][chng_idx], cost[i])
        
        # Floyd-Warshall algorithm to find all-pairs shortest paths
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if cost_matrix[i][j] > cost_matrix[i][k] + cost_matrix[k][j]:
                        cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]
        
        # Calculate total cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if cost_matrix[s_idx][t_idx] == inf:
                return -1
            total_cost += cost_matrix[s_idx][t_idx]
        
        return total_cost
