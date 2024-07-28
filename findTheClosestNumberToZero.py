from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_distance = float("inf")
        ans = 0
        for num in nums:
            if abs(num) < min_distance:
                ans = num
                min_distance = abs(num)

            elif abs(num) == min_distance:
                ans = max(ans, num)
        
        return ans
