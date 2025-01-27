# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]


##########
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        ans = float("inf")

        while left <= right:
            mid = (left + right) // 2
            if nums[left]<= nums[mid]:
                ans = min(ans, nums[left])
                left = mid +1
            
            if nums[mid] <= nums[right]:
                ans = min(ans, nums[mid])
                right = mid -1

        return ans 
