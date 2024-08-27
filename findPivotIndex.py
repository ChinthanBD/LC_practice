# https://leetcode.com/problems/find-pivot-index/submissions/1370282307/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Initialize left_sum to 0
        left_sum = 0
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # Calculate the right_sum by subtracting left_sum and nums[i] from total_sum
            right_sum = total_sum - left_sum - nums[i]
            
            # If left_sum equals right_sum, we have found the pivot index
            if left_sum == right_sum:
                return i
            
            # Update left_sum by adding the current element
            left_sum += nums[i]
        
        # If no pivot index is found, return -1
        return -1
