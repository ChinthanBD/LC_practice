# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr = 0

        for g in gain:
            curr += g
            ans = max(ans, curr)

        return ans
