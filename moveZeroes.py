# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        
        # If the current element is not 0, then we need to append it just in front of the last non-zero element we found. 
        for current in range(len(nums)):
            if nums[current] != 0:
                # Swap the elements
                nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
        


        
