# https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mpp = {}

        for i in nums:
            if i in mpp:
                return i
            else:
                mpp[i] = 1

        ########################################
        ## below less efficient (o(nLog(n))+o(N))
        # nums.sort()

        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
