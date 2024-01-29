# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # vol = 0
        # for i in range(len(height)):
        #     left_max = max(height[:i+1])
        #     right_max = max(height[i:])
        #     vol += min(left_max, right_max) - height[i]
        # return vol
        #########################

        vol = 0
        n = len(height)
        right = n-1
        left = 0
        right_max =0 
        left_max =0

        while left <= right:
            if left_max<= right_max:
                left_max = max(left_max, height[left])
                vol += left_max -  height[left]
                left +=1
            else:
                right_max = max(right_max, height[right])
                vol += right_max - height[right]
                right -=1
        return vol

        