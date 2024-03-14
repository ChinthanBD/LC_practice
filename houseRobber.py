# https://www.codingninjas.com/studio/problems/house-robber_839733?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from os import *
from sys import *
from collections import *
from math import *

def houseRobber(valueInHouse):
    # Write your function here.
    n = len(valueInHouse)
    if n == 0:
        return 0
    if n == 1:
        return valueInHouse[0]

    prev2 = 0
    prev = valueInHouse[0]

    for i in range(1, n - 1):
        pick = valueInHouse[i] + prev2
        non_pick = prev
        curri = max(pick, non_pick)
        prev2 = prev
        prev = curri
    no_pick_n = prev

    prev2 = 0
    prev = valueInHouse[1]

    for i in range(2, n):
        pick = valueInHouse[i] + prev2
        non_pick = prev
        curri = max(pick, non_pick)
        prev2 = prev
        prev = curri
    no_pick_0 = prev

    return max(no_pick_n, no_pick_0)