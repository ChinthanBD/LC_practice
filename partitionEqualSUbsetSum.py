# https://www.naukri.com/code360/problems/partition-equal-subset-sum_892980?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from typing import List, int, bool
def canPartition(arr: List[int], n: int)-> bool:
    # Calculate the total sum of the array
    s = sum(arr)
    
    # If the sum is odd, it's not possible to partition it into two equal subsets
    if s % 2 != 0:
        return False

    # Calculate the target sum which each subset should sum up to
    target = s // 2
    
    # Initialize the previous dictionary with a key 0 to True (0 sum is always possible)
    prev = {0: True}

    # If the first element is less than or equal to the target, set it in the previous dictionary
    if arr[0] <= target:
        prev[arr[0]] = True

    # Iterate over the rest of the elements in the array
    for i in range(1, n):
        # Initialize the current dictionary for this iteration
        curr = {0: True}
        
        # Iterate over all possible sums from 0 to target
        for k in range(target + 1):
            # Check if not picking the current element achieves the sum k
            nonPick = prev.get(k, False)
            pick = False
            
            # Check if picking the current element achieves the sum k
            if arr[i] <= k:
                pick = prev.get(k - arr[i], False)
            
            # Update the current dictionary with the result of picking or not picking the element
            curr[k] = pick or nonPick
        
        # Move to the next iteration by updating prev to be curr
        prev = curr
    
    # Return whether the target sum is achievable
    return prev.get(target, False)
