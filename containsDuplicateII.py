# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mpp = {}

        for i, num in enumerate(nums):
            if num in mpp:
                if i - mpp[num] <= k:
                    return True
            mpp[num] = i

        return False
