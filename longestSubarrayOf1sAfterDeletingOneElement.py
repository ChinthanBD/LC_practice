# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/1390218327/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0  # Left pointer of the window
        zeroes = 0  # Counter for zeroes in the window
        max_len = 0  # Variable to store the maximum length
        
        for r in range(len(nums)):  # Right pointer of the window
            if nums[r] == 0:
                zeroes += 1  # Increment zero counter if we encounter a zero
            
            # If we have more than 1 zero, shrink the window from the left
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1  # Move the left pointer to shrink the window
            
            # Calculate the maximum length (subtract 1 to account for removing one element)
            max_len = max(max_len, r - l)
        
        return max_len
