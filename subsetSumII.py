# https://leetcode.com/problems/subsets-ii/
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def generate_subsets(index, current_subset):
            if index == len(nums):
                # Add the current subset to the result
                ans.append(current_subset.copy())
                return
            
            # Include the current element
            current_subset.append(nums[index])
            generate_subsets(index + 1, current_subset)
            current_subset.pop()
            
            # Skip duplicates
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            # Exclude the current element
            generate_subsets(index + 1, current_subset)
        
        nums.sort()  # Sort the input list to handle duplicates
        ans = []
        generate_subsets(0, [])
        return ans