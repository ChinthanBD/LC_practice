# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                ans[i] = True
            else:
                ans[i] = False
        
        return ans