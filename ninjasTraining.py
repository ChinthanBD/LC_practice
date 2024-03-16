# https://www.codingninjas.com/studio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from typing import *

# def ninjaTraining(n: int, points: List[List[int]]) -> int:

#     # Write your code here.
    # def maxMerit(day, prev_task):
    #     if day == 0:
    #         maxi = 0
    #         for i in range(3):
    #             if i != prev_task:
    #                 maxi = max(points[0][i], maxi)
    #         return maxi
    #     maxi = 0
    #     for i in range(3):
    #         if i != prev_task:
    #             current_point = points[day][i] + maxMerit(day - 1, i)
    #             maxi = max(maxi, current_point)
    #     return maxi

    # return maxMerit(n - 1, 3)


###TLE for Above####

def ninjaTraining(n: int, points: List[List[int]]) -> List[int]:
    dp = [[-1] * 3 for _ in range(n)]

    def maxMerit(day, prev_task):
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != prev_task:
                    maxi = max(points[0][i], maxi)
            dp[0][prev_task] = maxi
            return dp[0][prev_task]
        
        if dp[day][prev_task] != -1:
            return dp[day][prev_task]
        
        maxi = 0
        for i in range(3):
            if i != prev_task:
                current_point = points[day][i] + maxMerit(day - 1, i)
                maxi = max(maxi, current_point)
        dp[day][prev_task] = maxi
        return dp[day][prev_task]

    return maxMerit(n - 1, -1) 

	
