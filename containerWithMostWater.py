# https://leetcode.com/problems/container-with-most-water/?envType=list&envId=9r108sl3
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        res = 0 
        while l<r:
            res = max(res, (r-l)* min(height[r], height[l]))
            if height[r] < height[l]:
                r-=1

            else:
                l+=1
        return res 

        