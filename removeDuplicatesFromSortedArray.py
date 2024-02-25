# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res_set = set(nums)
        res = list(res_set)
        res.sort()
        nums[:] = res # not used 'nums = res' because it just points nums to res(local reference) and not modify the actual nums array outside the function
        return len(res)
        ########################
        # i = 0
        # j = 0
        # count = 0
        # while i < len(nums):
        #     if nums[i] in nums[:i]:
        #         i+=1
        #         continue
        #     count+= 1
        #     nums[j]=nums[i]
        #     i+=1
        #     j+=1

        # return count