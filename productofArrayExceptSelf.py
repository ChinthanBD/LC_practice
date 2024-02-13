# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        res = [1] * n
        val = 1
        for i in range(1, n):
            val *= nums[i - 1]
            res[i] = val
        
        # Calculate products of all elements to the right of the current element and multiply them with the products from the left
        postres = 1
        for i in range(n - 2, -1, -1):
            postres *= nums[i + 1]
            res[i] *= postres

        return res


        
