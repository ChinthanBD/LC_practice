# https://www.codingninjas.com/studio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp = [None] * n
    


    def func(step, dp, heights):
        if step == 0:
            return 0
        if dp[step] is not None:
            return dp[step]

        left = func(step-1, dp, heights) + abs(heights[step] - heights[step-1])
        right = float("inf")

        if step > 1:
            right = func(step-2, dp, heights) + abs(heights[step] - heights[step-2])

        dp[step] = min(left, right)
        return dp[step]

    return func(n-1, dp, heights)
