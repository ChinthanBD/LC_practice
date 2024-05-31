# https://www.naukri.com/code360/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM


from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    # Base case: if arr is empty or k is negative, return 0
    if not arr or k < 0:
        return 0

    # Initializing the previous row with base cases
    prev_row = {0: 1}  # There's one way to make the sum 0 (by picking nothing)
    if arr[0] <= k:
        prev_row[arr[0]] = prev_row.get(arr[0], 0) + 1

    # Iterate through the rest of the array
    for i in range(1, len(arr)):
        curr_row = {}
        for target in range(k+1):
            nonPick = prev_row.get(target, 0)  # Number of ways to get `target` without current element
            pick = 0
            if target >= arr[i]:
                pick = prev_row.get(target - arr[i], 0)  # Number of ways to get `target` with current element

            curr_row[target] = pick + nonPick
        prev_row = curr_row

    return prev_row.get(k, 0)
