# https://leetcode.com/problems/sort-colors/
# Dutch national flag problem   
# 0 - (Low-1) ---> 0
# low - (mid-1) ---> 1
# high+1 - n-1 ---> 2
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        mid = 0
        high = n -1

        while high>=mid:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1
