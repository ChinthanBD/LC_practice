# https://leetcode.com/problems/maximum-distance-in-arrays/?envType=daily-question&envId=2024-08-16
from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize the minimum and maximum with the first array's elements
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            # Calculate the possible max distances with the current array
            max_distance = max(max_distance, abs(arrays[i][-1] - min_value), abs(max_value - arrays[i][0]))
            
            # Update the global minimum and maximum with the current array's elements
            min_value = min(min_value, arrays[i][0])
            max_value = max(max_value, arrays[i][-1])
        
        return max_distance
