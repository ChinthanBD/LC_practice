# https://leetcode.com/problems/max-consecutive-ones/description/
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentCount +=1
            else:
                currentCount = 0
            maxCount = max(currentCount, maxCount)
        return maxCount