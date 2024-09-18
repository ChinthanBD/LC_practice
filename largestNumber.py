# https://leetcode.com/problems/largest-number/submissions/1394460929/?envType=daily-question&envId=2024-09-18
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def customCompare(n1, n2):
            if n1 + n2 > n2 + n2:
                return -1
            return 1
        
        nums.sort(key=cmp_to_key(customCompare))
    
        if nums[0] == '0':
            return '0'
        
        return ''.join(nums)
