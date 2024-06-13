# https://www.naukri.com/code360/problems/minimum-elements_3843091?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dpseries&leftPanelTabValue=PROBLEM
from typing import List

def minimumElements(num: List[int], x: int) -> int:
    # Initialize the previous array with "infinity" representing unreachable states
    prev = [float('inf')] * (x + 1)
    # Zero elements are needed to reach the sum of zero
    prev[0] = 0

    # Initialize prev for the first coin
    for t in range(x + 1):
        if t % num[0] == 0:
            prev[t] = t // num[0]
            
    # Iterate over each coin
    for i in range(len(num)):
        curr = [float('inf')] * (x + 1)
        # Iterate over each possible sum up to x
        for target in range(x + 1):
            nonTake = prev[target]
            take = float('inf')
            if target >= num[i]:
                take = curr[target - num[i]] + 1
            
            curr[target] = min(take, nonTake)
        prev = curr
    
    # If prev[x] is still infinity, it means x is unreachable with given coins
    return prev[x] if prev[x] != float('inf') else -1
