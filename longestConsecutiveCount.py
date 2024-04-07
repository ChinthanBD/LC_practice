from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res = 1  # Initialize result to at least 1 for the case when there's only one element
        curr_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            elif nums[i - 1] + 1 == nums[i]:
                curr_count += 1
            else:
                curr_count = 1  # Reset the count for non-consecutive elements
            
            res = max(res, curr_count)

        return res
