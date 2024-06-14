# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findPivot(left, right, nums):
            while left<right:
                mid = (left + right) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else: 
                    right = mid
                
            return left

        
        def binarySearch(l, r, nums, target):
            while l<=r:
                mid =  (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        if not nums:
            return -1
        left, right = 0, len(nums) -1
        pivot = findPivot(left, right, nums)


        if nums[pivot]<= target <= nums[right]:
            return binarySearch(pivot, right, nums, target)
        else:
            return binarySearch(0, pivot-1, nums, target)
