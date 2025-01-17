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


# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup_dict={}
        for i in range(len(nums)):
            if nums[i] in lookup_dict and abs(lookup_dict[nums[i]] - i)<=k:
                return True
            
            lookup_dict[nums[i]] = i
        
        return False
