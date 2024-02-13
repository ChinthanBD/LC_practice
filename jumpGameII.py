# https://leetcode.com/problems/jump-game-ii/description/
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=0
        r=0
        while r<len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r=farthest
            res+=1

        return res

        ###############
        # if len(nums) == 1:
        #     return 0
        
        # max_reachable = 0
        # jumps = 0
        # current_max_reach = 0
        
        # for i in range(len(nums) - 1):
        #     current_max_reach = max(current_max_reach, i + nums[i])
            
        #     if i == max_reachable:
        #         jumps += 1
        #         max_reachable = current_max_reach
                
        #         if max_reachable >= len(nums) - 1:
        #             return jumps
        
        # return jumps