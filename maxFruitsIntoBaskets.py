# https://leetcode.com/problems/fruit-into-baskets/description/
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        n = len(fruits)

        mpp = {}
        maxFruits = 0

        while r<n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1

            if len(mpp)>2:
                while len(mpp)>2:
                    mpp[fruits[l]] = mpp.get(fruits[l]) - 1
                    if mpp[fruits[l]] == 0:
                        del mpp[fruits[l]]
                    l+=1

            maxFruits =  max(maxFruits, r-l+1)
            r+=1

        return maxFruits           
                    