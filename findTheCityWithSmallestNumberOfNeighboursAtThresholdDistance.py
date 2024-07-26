# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/?envType=daily-question&envId=2024-07-26
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity and set 0 for self-loops
        distances = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0

        # Set initial distances based on the given edges
        for u, v, w in edges:
            distances[u][v] = w
            distances[v][u] = w
        
        # Floyd-Warshall algorithm to find all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        # Find the city with the smallest number of reachable cities within the distance threshold
        min_reachable = float('inf')
        result_city = -1
        
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if distances[i][j] <= distanceThreshold)
            # Check for tie-breaking condition and update the result city accordingly
            if reachable_count < min_reachable or (reachable_count == min_reachable and i > result_city):
                min_reachable = reachable_count
                result_city = i

        return result_city
