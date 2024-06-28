# https://leetcode.com/problems/maximum-total-importance-of-roads/description/?envType=daily-question&envId=2024-06-28
from collections import defaultdict
from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance = defaultdict(int)
        
        # Count the number of connections for each city
        for u, v in roads:
            importance[u] += 1
            importance[v] += 1
        
        # Sort cities based on their number of connections in descending order
        sorted_cities = sorted(importance.items(), key=lambda x: x[1], reverse=True)
        
        # Assign the highest available values to the cities with the most connections
        value = n
        city_values = [0] * n
        for city, _ in sorted_cities:
            city_values[city] = value
            value -= 1
        
        # Assign remaining values to cities with no connections
        for i in range(n):
            if city_values[i] == 0:
                city_values[i] = value
                value -= 1
        
        # Calculate the total importance of all roads
        total_importance = 0
        for u, v in roads:
            total_importance += city_values[u] + city_values[v]
        
        return total_importance