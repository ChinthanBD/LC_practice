# https://leetcode.com/problems/subarray-product-less-than-k/submissions/1215740388/
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        product = 1
        res = 0
        for r in range(len(nums)):
            product *=nums[r]

            while l<=r and product>=k:
                product = product // nums[l]
                l+=1

            res  += r- l +1
        return res
