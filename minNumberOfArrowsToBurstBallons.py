# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1226010901/?envType=study-plan-v2&envId=top-interview-150
from typing import list
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if curr[0]<= prev[1]:
                res -=1
                prev = [curr[0], min(curr[1],prev[1])]
            else:
                prev = curr
            
        return res

