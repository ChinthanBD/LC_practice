# https://leetcode.com/problems/max-consecutive-ones-iii/description/
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        maxOnes = 0
        n = len(nums)
        zeroCount = 0
        while r < n:
            if nums[r] == 0:
                zeroCount+=1
                while zeroCount>k:
                    if nums[l] == 0:
                        zeroCount -=1
                    l+=1
            maxOnes = max(maxOnes, r - l + 1)
            r+=1
        return maxOnes                