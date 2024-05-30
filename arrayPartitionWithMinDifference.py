# https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM

from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    # write your code here
    s = sum(arr)

    prev_row = {0:True, arr[0]: True}

    ans = float("inf")

    for i in range(1, len(arr)):
        curr_row = {0:True}
        for target in range(s//2+1):
            nontake = prev_row.get(target, False)
            take = False
            if target>=arr[i]:
                take = prev_row.get(target-arr[i], False)
            
            if take or nontake:
                curr_row[target] = True
                ans = min(ans, abs(s - 2 * target))
        prev_row = curr_row
    
    return ans
