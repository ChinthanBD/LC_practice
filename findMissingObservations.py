# leetcode problem
#https://leetcode.com/problems/find-missing-observations/?envType=daily-question&envId=2024-09-05
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (m+n)
        missing_sum = total_sum - sum(rolls)

        average_per_pos = missing_sum/n
        if average_per_pos > 6 or average_per_pos <1:
            return []
        
        res = []
        while n:
            dice = min(6, missing_sum - n +1)
            res.append(dice)
            missing_sum -= dice
            n-=1
        
        return res