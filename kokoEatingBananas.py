import math
# https://leetcode.com/problems/koko-eating-bananas/description/
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            eating_rate = (r + l) // 2
            curr_hrs = 0
            for pile in piles:
                curr_hrs += math.ceil(pile / eating_rate)
        
            if curr_hrs <= h:
                ans = min(eating_rate, ans)
                r = eating_rate - 1
            else:
                l = eating_rate + 1
        
        return ans


        