# https://leetcode.com/problems/rotate-array/
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # nums[:] = nums[len(nums)-k: ] + nums[: len(nums)-k]
        
        #############################
        
        n = len(nums)
        k = k%n

        # Reverse the entire array
        self.arr_rev(nums, 0, n-1)

        # Reverse the first k elements
        self.arr_rev(nums, 0, k-1)

        # Reverse the remaining elements after k
        self.arr_rev(nums, k, n-1)

    def arr_rev(self,arr,l,r):
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1