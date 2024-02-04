# https://leetcode.com/problems/maximum-subarray/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # max_sum = -9999999999
        # sum = 0
        # for num in nums:
        #     sum += num

        #     if sum > 0:
        #         max_sum = max(sum, max_sum)
        #     else:
        #         sum = 0
        # return max_sum

        ####Above fails for all -ve elements

        if not nums:
            return None

        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, num+current_sum)           
            max_sum = max(max_sum, current_sum)
        return max_sum