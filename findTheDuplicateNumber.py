# https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # mpp = {}

        # for i in nums:
        #     if i in mpp:
        #         return i
        #     else:
        #         mpp[i] = 1

        ########################################
        ## below less efficient (o(nLog(n))+o(N))
        # nums.sort()

        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]

        ############# Floyd's Algo(Linked list approach)

        fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
        
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

