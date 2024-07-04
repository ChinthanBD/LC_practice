# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/?envType=daily-question&envId=2024-07-03
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # With 3 or fewer moves, we can make all elements equal

        nums.sort()
    
    # Possible scenarios to minimize the range
        return min(nums[-1] - nums[3],  # Remove the 3 smallest elements
                nums[-2] - nums[2],  # Remove the 2 smallest and the largest element
                nums[-3] - nums[1],  # Remove the smallest and the 2 largest elements
                nums[-4] - nums[0])  # Remove the 3 largest elements