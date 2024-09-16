# https://leetcode.com/problems/minimum-time-difference/?envType=daily-question&envId=2024-09-16
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def timeToMins(t):
            h, m = map(int, t.split(':'))
            return h * 60 + m
        

        res = (
            24 * 60 - timeToMins(timePoints[-1] )
            + timeToMins(timePoints[0])
        )

        for i in range(len(timePoints) -1):
            curr = timePoints[i+1]
            prev = timePoints[i]

            diff = timeToMins(curr) - timeToMins(prev)
            
            res= min(res, diff)
            if diff == 0:
                return 0
        return res
