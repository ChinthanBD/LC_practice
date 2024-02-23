# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        r = 0 
        n = len(nums)
        res = float('inf')
        curr_sum = 0  # Initialize the current sum of the window
        
        while r < n:  
            curr_sum += nums[r] 
            while curr_sum >= target:  
                res = min(res, r - l + 1)  
                curr_sum -= nums[l]  
                l += 1  
            r += 1  
        
        return res if res != float('inf') else 0  