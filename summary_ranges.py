# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return ""
        start = 0
        end = 0
        current = 1
        res = []
        while current < len(nums):
            if nums[current] != nums[current-1] + 1:
                if start == end:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                start = current
            end = current
            current += 1
        if start == end:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[end]))
        return res

                
