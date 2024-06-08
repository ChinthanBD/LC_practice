# https://leetcode.com/problems/binary-search/

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l<=r:
            mid = (l+r)//2
            curr_ele = nums[mid]
            if curr_ele == target:
                return mid
            elif curr_ele < target:
                l = mid +1
            else:
                r = mid -1
            
        return -1
        